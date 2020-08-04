import os, glob, shutil, os
from PIL import Image

dir = 'result/last_r/'

for filename in os.listdir(dir):
    name = os.path.basename(filename)
    sp = name.split("_fg")
    sn = sp[0]
    old = dir + filename
    new_name = str(sn) + str('.png')
    new2 = dir + new_name
    os.rename(old, new2)
