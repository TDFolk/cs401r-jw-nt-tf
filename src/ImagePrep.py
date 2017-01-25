from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps
#import cv2

MEDIAN_FILTER_SIZE = 3

def prep(src, dest):

    # open image
    img = Image.open(src)

    # Reduce Image Size or create image pyramid


    # Histogram Stretch Image
    img = ImageOps.autocontrast(img)

    # Median Filter (get rid of text, background noise).
    img = img.filter(ImageFilter.MedianFilter(MEDIAN_FILTER_SIZE))

    # Automatically threshold image into foreground, background

    imgout = ImageOps.equalize(img)
    return imgout
