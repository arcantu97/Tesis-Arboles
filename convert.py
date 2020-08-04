from glob import glob                                                           
import cv2, os
directory = glob('train/Trinidad/*.JPG')

for unFile in directory:
    img = cv2.imread(unFile)
    cv2.imwrite(unFile[:-3] + 'png', img)
    if unFile[:-3] != "png":
        os.remove(unFile)
