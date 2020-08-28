import glob, os, ntpath, cv2
from PIL import Image

foldersName = []
for folder in glob.iglob("../data/dataset/test/*", recursive=True):
    foldersName.append(folder.replace('\\', '/') + "/*")
for path in foldersName:
    for item in glob.iglob(path, recursive=True):
        item.replace('\\', '/')
        im = cv2.imread(item)
        w, h, c = im.shape
        if(w == 6000 and h == 4000):
            print('Rotating: ', item)
            imageToFix = Image.open(item)
            rotated = imageToFix.rotate(-180)
            rotated.save(item)