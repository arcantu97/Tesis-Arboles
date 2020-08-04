from __future__ import print_function
from PIL import Image
import os.path, glob, time


void = (0, 0, 0, 255)
green = (38, 230, 0, 0)
yellow = (254, 230, 0, 0)
blue = (0, 77, 229, 0)
annotation = [green, yellow, blue] # annotation colors
threshold = 70 # adjustable parameter for annotation removal
margin = 0 # adjustable parameter for ground removal


for filename in glob.glob('Cilantrillo/*.png'):
    img = Image.open(filename).convert('RGBA')
    pix = img.load()
    (w, h) = img.size
    for x in range(w):
        for y in range(h):
            p = pix[x, y]
            (r, g, b, a) = p
            discard = False
            if a > 0: # only non-blank pixels are processed        
                for ann in annotation:
                    diff = sum([(p[i] - ann[i])**2 for i in range(3)]) # rgb
                if diff < threshold:
                    discard = True
                    break
            if discard or g < max(r, b) + margin: # not dominantly green
                pix[x, y] = void                
                
    img.save(filename.replace('.', '_fg.'))



    