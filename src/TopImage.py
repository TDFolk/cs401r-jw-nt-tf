import sys
import ImagePrep as imgp
import Crop
import cv2

def CropTopImage(src):

    # prepare image
    original = cv2.imread(src,0)
    imgout = imgp.prep(original)

    #crop
    imgout = Crop.crop(imgout, original)

    # save
    cv2.imwrite("result.jpg", imgout)

# TODO: validate command line arguements
img = sys.argv[1]

# Crop
CropTopImage(img)