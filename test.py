# https://gogul09.github.io/software/image-classification-python

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from PIL import Image
from math import ceil
import matplotlib.pyplot as plt
import mahotas
import numpy as np
import glob
import h5py
import cv2
import os
import time

def fd_hu_moments(image): # feature-descriptor-1: Hu Moments
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    feature = cv2.HuMoments(cv2.moments(image)).flatten()
    return feature

def fd_haralick(image): # feature-descriptor-2: Haralick Texture
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    haralick = mahotas.features.haralick(gray).mean(axis=0)
    return haralick

def fd_histogram(image, mask=None): # feature-descriptor-3: Color Histogram
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hist  = cv2.calcHist([image], [0, 1, 2], None, [bins, bins, bins], [0, 256, 0, 256, 0, 256])
    cv2.normalize(hist, hist)
    return hist.flatten()

test_size = 0.3
bins = 16

h5f_data = h5py.File('output/data2.h5', 'r')
h5f_label = h5py.File('output/labels2.h5', 'r')
global_features_string = h5f_data['dataset_2']
global_labels_string = h5f_label['dataset_2']
global_features = np.array(global_features_string)
global_labels = np.array(global_labels_string)
h5f_data.close()
h5f_label.close()

(trainDataGlobal, testDataGlobal, trainLabelsGlobal, testLabelsGlobal) = train_test_split(np.array(global_features),
                                                                                          np.array(global_labels),
                                                                                          test_size=test_size)
clf  = RandomForestClassifier(n_estimators=200)
clf.fit(trainDataGlobal, trainLabelsGlobal)

test_path = "dataset/test/ngf"
labelMap = {0: "pino", 1: "abies", 2: "encino"} # blue green yellow
clipWidth = 300
clipHeight = 300
threshold = 0.5 # proportion of absent pixels allowed
void = (0, 0, 0, 255)
sep = 100
box = {'abies': (38, 230, 0), 'encino': (254, 230, 0), 'pino': (0, 77, 229)} 
for label in box: # BGR for OpenCV
    (r, g, b) = box[label]
    box[label] = (b, g, r)
counters = {0: 0, 1: 0, 2: 0}
for f in glob.glob(test_path + "/*.png" ):
    fullImage = cv2.imread(f)
    height, width, channels = fullImage.shape
    print('Testing on image', f)
    start = time.time()
    for x in range(sep, width - sep, clipWidth + sep):
        for y in range(sep, height - sep, clipHeight + sep):
            skip = False
            encountered = 0        
            image = fullImage[y : y + clipHeight, x : x + clipWidth] 
            img = Image.open(f)
            name = os.path.basename(f)
            pix = img.load()
            allowed = int(ceil(clipWidth * clipHeight * threshold))
            fv_hu_moments  = fd_hu_moments(image) 
            fv_haralick    = fd_haralick(image)
            fv_histogram   = fd_histogram(image)
            global_feature = np.hstack([fv_histogram, fv_haralick, fv_hu_moments]) 
            prediction     = clf.predict(global_feature.reshape(1,-1))[0]
            kind = labelMap[prediction]
            counters[prediction] += 1
            color = box[kind]
            for x0 in range(clipWidth):
                for y0 in range(clipHeight):
                    p = pix[x0 + x, y0 + y]
                    (r, g, b, a) = p
                    if p == void:
                        encountered += 1
                        if encountered > allowed:
                            skip = True
                            break
                if skip:
                    break
            if not skip:
                cv2.rectangle(fullImage, (x, y), (x + clipWidth, y + clipHeight), color, 30) 
                cv2.putText(fullImage, kind, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 3.0, (255, 255, 255), 3)
            filename = 'result/' + name 
    cv2.imwrite(filename, fullImage)
    end = time.time()
    result = end - start
print(counters)
print('processed at: ', str(result))

  
    
