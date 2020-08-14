import os, glob, shutil

dir = 'resultC/'

i = 6077
for filename in os.listdir(dir): 
    dst ="Cilantrillo_InkedDSC0" + str(i) + "_LI.png"
    src = dir + filename 
    dst = dir + dst  
    os.rename(src, dst) 
    i += 1
