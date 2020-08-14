import glob
import os
import ntpath
from PIL import Image

counter = 0
deleted = 0

for treeFile in os.listdir("train/Cilantrillo"):
    filename = os.path.abspath(os.path.join("train/Cilantrillo", treeFile))
    name, ext = os.path.splitext(treeFile)
    img = Image.open(filename)
    img = img.convert('RGBA')
    pix = img.load()
    (w, h) = img.size

    # <!--- Colour configuration ---!>
    void = (0, 0, 0, 255)
    green = (38, 230, 0, 0)
    yellow = (254, 230, 0, 0)
    blue = (0, 77, 229, 0)
    annotation = [green, yellow, blue] # annotation colors
    threshold = 30 # adjustable parameter for annotation removal
    margin = 0 # adjustable parameter for ground removal

    print("Removing foreground of " + name)
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
    counter += 1
    if treeFile[-5:] != "g.png":
        name, ext = os.path.splitext(treeFile)
        os.remove(filename)
        deleted += 1
print("Finished with " + str(counter) + " files edited and " + str(deleted) + " deleted")




