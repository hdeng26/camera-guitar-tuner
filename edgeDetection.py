import numpy 
import cv2
import math
import argparse

#main function
gray = cv2.imread('1.png',0)



    #30 and 150 is the threshold, larger than 150 is considered as edge,
    #less than 30 is considered as not edge
canny = cv2.Canny(gray, 30, 150)

canny = numpy.uint8(numpy.absolute(canny))
    #display two images in a figure
cv2.imshow("Edge detection by Canny", numpy.hstack([gray,canny]))

cv2.imwrite("1_edge_by_canny.jpg", canny)


if(cv2.waitKey(0)==27):
     cv2.destroyAllWindows()

