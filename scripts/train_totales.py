# https://gogul09.github.io/software/image-classification-python
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import mahotas
import cv2
import os
import h5py
import datetime
import glob
from PIL import Image

fixed_size = tuple((300, 300))
train_path = "exp/rect"
bins = 16

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

def getSizePath(path):
    size = 0
    for file in glob.iglob(path, recursive=True):
        size+= 1
    return size

def MaxValue():
    sizes = []
    for training_name in train_labels:
        dire = os.path.join(train_path, training_name)
        size = getSizePath(dire + "/*.png")
        sizes.append(size)
    return max(sizes)


train_labels = ['green', 'blue', 'yellow']
images_per_class = 1600 
global_features = []
labels = []
i, j = 0, 0
c = 0
for training_name in train_labels:
    dire = os.path.join(train_path, training_name)
    size = getSizePath(dire + "/*.png")
    while size < MaxValue():
        for x in range(0, size):
            filename = dire + "/img_" + str(x) + ".png"
            print(filename)
            print("{} of {}".format(size, MaxValue()))
            if(size == MaxValue()):
                break
            else:
                size += 1
                image = cv2.imread(filename)
                img = cv2.flip(image, 1)
                image = cv2.resize(image, fixed_size)
                cv2.imwrite(dire + "/img_" + str(size) + ".png", img)
print('Start at: ', datetime.datetime.now())
for training_name in train_labels:
    dire = os.path.join(train_path, training_name)
    size = getSizePath(dire + "/*.png")
    print('processing directory', dire)
    k = 1
    for x in range(0, size):
        filename = dire + "/img_" + str(x) + ".png"
        image = cv2.imread(filename)
        print(filename)
        image = cv2.resize(image, fixed_size)
        fv_hu_moments = fd_hu_moments(image)
        fv_haralick   = fd_haralick(image)
        fv_histogram  = fd_histogram(image)
        global_feature = np.hstack([fv_histogram, fv_haralick, fv_hu_moments])
        labels.append(training_name)
        global_features.append(global_feature)
        i += 1
        k += 1
    j += 1


print("[STATUS] feature vector size", np.array(global_features).shape)
print("[STATUS] training labels", np.array(labels).shape)
targetNames = np.unique(labels)
le = LabelEncoder()
target = le.fit_transform(labels)
cle =  list(set(target))
print(cle, le.inverse_transform(cle))
print("[STATUS] target labels shape", target.shape)
scaler = MinMaxScaler(feature_range=(0, 1))
rescaled_features = scaler.fit_transform(global_features)
h5f_data = h5py.File('output_reflexion/data2.h5', 'w')
h5f_data.create_dataset('dataset_2', data=np.array(rescaled_features))
h5f_label = h5py.File('output_reflexion/labels2.h5', 'w')
h5f_label.create_dataset('dataset_2', data=np.array(target))
h5f_data.close()
h5f_label.close()
print('Ends at: ', datetime.datetime.now())