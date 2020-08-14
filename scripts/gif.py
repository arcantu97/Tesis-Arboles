# import OpenCV file 
import cv2, os.path, glob
from PIL import Image

dir_original = 'Original/'
dir_original2 = 'Original/'
dir_combinadas = 'combinadas/'
dir_nofondo = 'Marcas/'
images = []
for image in glob.glob(dir_original + "/*.png"):
    name_original = os.path.basename(image)
    im1 = Image.open(image)
    for image2 in glob.glob(dir_nofondo + "/*.png"):
        name_nfo = os.path.basename(image2)
        im2 = Image.open(image2)
        for image3 in glob.glob(dir_original2 + "/*.png"):
            name_original2 = os.path.basename(image3)
            im3 = Image.open(image3)
            for image4 in glob.glob(dir_combinadas + "/*.png"):
                name_comb = os.path.basename(image4)
                im4 = Image.open(image4)
                if name_original == name_nfo and name_original == name_original2 and name_original == name_comb and name_nfo ==  name_original and name_nfo == name_original2 and name_nfo == name_comb and name_original2 ==  name_original and name_original2 == name_nfo and name_original2 == name_comb and name_comb ==  name_original and name_comb == name_nfo and name_comb == name_original2:
                    images.append(im1)
                    images.append(im2)
                    images.append(im3)
                    images.append(im4)
                    filename = name_original
                    sp = filename.split(".png")
                    new_name = sp[0] + ".gif"
                    images[0].save(new_name, save_all=True, append_images=images[1:], duration=1000, loop=0)                    
                    images.clear()
                else:
                    pass


