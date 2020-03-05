import numpy 
import cv2
import math
import argparse
import sys

numpy.set_printoptions(threshold=sys.maxsize)

#main function
img = cv2.imread('1_edge_by_canny.jpg',0)

h = img.shape[0]
w = img.shape[1]
# loop over the image, pixel by pixel
for y in range(0, h):
    for x in range(0, w):
        # threshold the pixel
        if img[y, x] >= 128:  
            img[y, x] = 255 
        if img[y, x] <=128: 
            img[y, x] = 0
print(img)
cv2.imwrite ('output.png', img)
cv2.imshow('output',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(gray)

