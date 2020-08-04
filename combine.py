import cv2, os, glob
from PIL import Image

dir_mask = 'result/last_r'
dir_base = 'Original/last_r'

for image in glob.glob(dir_base + "/*.png"):
    name_simple = os.path.basename(image)
    for image2 in glob.glob(dir_mask + "/*.png"):
        name_mask = os.path.basename(image2)
        if name_simple == name_mask:
            simple = Image.open(image).convert('RGBA')
            mask = Image.open(image2).convert('RGBA')
            datas = mask.getdata()
            newData = []
            for item in datas:
                if item[0] == 0 and item[1] == 0 and item[2] == 0:
                    newData.append((255, 255, 255, 0))
                else:
                    newData.append(item)
            mask.putdata(newData)
            new = Image.new('RGBA', (6000,4000), (0,0,0,0))
            new.paste(simple, (0,0))
            new.paste(mask, (0,0), mask=mask)
            new.save('result/Trinidad/' + name_simple)
