import numpy as np
import cv2
from matplotlib import pyplot as plt
'''
img = cv2.imread('test1.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray,50,0.01,10)
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)

cv2.imshow('output',img)
'''


img = cv2.imread('test1.jpg',0)

# Initiate STAR detector
orb = cv2.ORB_create(500)

# find the keypoints with ORB
kp, des = orb.detectAndCompute(img, None)


# draw only keypoints location,not size and orientation
img2 = cv2.drawKeypoints(img,kp, np.array([]),color=(0,255,0), flags=0)
cv2.imshow('a',img2)
