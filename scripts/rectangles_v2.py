from collections import defaultdict
from PIL import Image
from math import ceil
import os, glob

threshold = 0.005 # proportion of absent pixels allowed
counter = defaultdict(int)
dirname = 'blue'
directory = os.fsencode(dirname)
tw = 150
th = 150
step = 25
void = (0, 0, 0, 255)
allowed = int(ceil(tw * th * threshold))

for treeFile in os.listdir("yellow"):
     filename = os.path.abspath(os.path.join("yellow", treeFile))
     name, ext = os.path.splitext(treeFile)
     label = name.split('_')[0]
     img = Image.open(filename)
     (w, h) = img.size
     pix = img.load()
     for x0 in range(0, w - tw, step):
          for y0 in range(0, h - th, step):
               skip = False
               encountered = 0
               for x in range(tw):
                    for y in range(th):
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
                    counter[label] += 1
                    box = (x0, y0, x0 + tw, y0 + th)                         
                    img.crop(box).save('rect/{:s}_{:d}_fg.png'.format(label, counter[label]))
                    print(x0, y0, 'stored')      
    