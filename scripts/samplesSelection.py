from PIL import Image
from shutil import copyfile
import glob, os, ntpath, cv2, shutil, random

path_OS = '../data/dataset/test/ngf/'
globalPath = '../data/dataset/test/ngf/*.png'
newFolder = 'D:\Experimentos - tesis\data\dataset\{}\experiments'.format('test')

def getSizePath(path):
    size = 0
    for file in glob.iglob(path, recursive=True):
        size+= 1
    return size

def pickFile(number):
    print(number)
    fileName = os.listdir(path_OS)[number]
    return fileName

size = getSizePath(globalPath)   
os.mkdir(newFolder)
for _ in range(30):
    value = random.randint(0, size)
    fileName = pickFile(value)
    for file in glob.iglob(globalPath, recursive=True):
        equalPath = '../data/dataset/test/ngf\{}'.format(fileName) 
        if(file == equalPath):
            shutil.copy2(equalPath, newFolder)
	