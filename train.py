# https://gogul09.github.io/software/image-classification-python
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import mahotas
import cv2
import os
import h5py
import time

fixed_size = tuple((300, 300))
train_path = "dataset/train"
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

train_labels = ['green', 'blue', 'yellow']
images_per_class = 5778 
global_features = []
labels = []
i, j = 0, 0

for training_name in train_labels:
    dire = os.path.join(train_path, training_name)
    print('processing directory', dire)
    start = time.time()
    k = 1
    for x in range(1, images_per_class + 1):
        filename = dire + "/image_" + str(x) + ".png"
        image = cv2.imread(filename)
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
    end = time.time()
    print('processed at: ', end - start)

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
h5f_data = h5py.File('output/data2.h5', 'w')
h5f_data.create_dataset('dataset_2', data=np.array(rescaled_features))
h5f_label = h5py.File('output/labels2.h5', 'w')
h5f_label.create_dataset('dataset_2', data=np.array(target))
h5f_data.close()
h5f_label.close()
