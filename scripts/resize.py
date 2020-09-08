from PIL import Image
import glob, os, ntpath, cv2
from resizeimage import resizeimage

for item in glob.iglob("../data/dataset/test/g_samp/*", recursive=True):
    imageToFix = Image.open(item)
    imageToFix = imageToFix.resize((500, 500), Image.ANTIALIAS)
    imageToFix.save(item)


