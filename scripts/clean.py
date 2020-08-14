import fnmatch, os, glob

for treeFile in glob.glob('rect/*.png'):
    if treeFile[-5:] != "0.png":
        os.remove(treeFile)
