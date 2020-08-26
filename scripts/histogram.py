import cv2
import numpy 
from PIL import Image
from matplotlib import pyplot as plt

img = cv2.imread('DSC06100.png')
color = ('b','g','r')

for i, c in enumerate(color):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color = c)
    plt.xlim([0,256])


plt.xlabel('Intensidad de iluminación', fontsize=20)
plt.ylabel('Cantidad de píxeles', fontsize=20)
plt.show()

image = Image.open('DSC06100.png')
new_image = image.resize((640, 480))
new_image.save('DSC06100.png')

cv2.destroyAllWindows()