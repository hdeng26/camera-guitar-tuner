import cv2
import numpy as np
import math

image = cv2.imread('test1.jpg')
print(image.shape)
print(image.shape[0]//2)
crop_img = image[0:image.shape[0]//2, 0:image.shape[1]//2]
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)