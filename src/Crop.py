import cv2
import numpy as np
np.set_printoptions(threshold=np.inf)
import sys

#def get_end_values(img, index):
#    axis = np.argmax(img, index)
#    max_value = np.max(axis)
#    axis[axis == 0] = 999999
#    min_value = np.min(axis)
#    return max_value.astype(int), min_value.astype(int)


#def crop(img, src):
#    max_x, min_x = get_end_values(img, 0)
#    max_y, min_y = get_end_values(img, 1)
#    print(max_x)
#    print(min_x)
#    print(max_y)
#    print(min_y )
#    print(img.shape)

#    imgout = src[min_x:max_x, min_y:max_y]
#    return imgout

def crop(img, src):
    sys.stdout=open("out.txt", "w")
    print(img)
    sys.stdout.close()

    def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
        """
        `img` should be the output of a Canny transform.

        Returns an image with hough lines drawn.
        """
        lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len,
                                maxLineGap=max_line_gap)
        line_img = np.zeros((*img.shape, 3), dtype=np.uint8)
        #draw_lines(line_img, lines)
        return line_img



    return img

