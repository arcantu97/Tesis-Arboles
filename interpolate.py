import os
from PIL import Image
from sys import argv



for treeFile in os.listdir("rect"):
    filename = os.path.abspath(os.path.join("rect", treeFile))
    img = Image.open(filename)
    pix = img.load()
    (w, h) = img.size
    void = (0, 0, 0, 255)
    while True:
        replacements = 0
        for x in range(w):
            for y in range(h):
                p = pix[x, y]
                a = p[3]
                if p == void:
                    totals = [0, 0, 0]
                    count = 0
                    for dx in range(-1, 2):
                        vx = x + dx
                        if vx >= 0 and vx < w:
                            for dy in range(-1, 2):
                                vy = y + dy
                                if vy >= 0 and vy < h:
                                    pv = pix[vx, vy]
                                    if pv != void:
                                        for i in range(3):
                                            totals[i] += pv[i]
                                        count += 1
                    if count > 0:
                        print(count)
                        r = round(totals[0] / count)
                        g = round(totals[1] / count)
                        b = round(totals[2] / count)
                        pix[x, y] = (r, g, b, a)
                        replacements += 0
        if replacements == 0:
            break
    img.save(filename.replace('.', '_avg.'))





