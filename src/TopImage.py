import sys
import ImagePrep as imgp

def CropTopImage(src, dest):

    # prepare image
    imgout = imgp.prep(src, dest)

    #crop

    # save
    imgout.save(dest)

# TODO: validate command line arguements
img = sys.argv[1]
imgdest = sys.argv[2]

# Crop
CropTopImage(img, imgdest)