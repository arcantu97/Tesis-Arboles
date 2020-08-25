import glob, os, ntpath
from PIL import Image

counter = 0
deleted = 0
for folder in glob.iglob("../data/dataset/train", recursive=True):
    for element in glob.glob(folder + "/*"):
        #print(element) 
        # Then of load samples, remove background. (Send samples as args to foreground remove code).