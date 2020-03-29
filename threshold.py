import cv2  
import numpy as np  
from matplotlib import pyplot as plt
import math


cap = cv2.VideoCapture("EADGBE.mp4")

ret1, frame1 = cap.read()
prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[...,1] = 255
countFrame = 0

while(1):
    ret2, frame2 = cap.read()
    if not ret1 or not ret2:
        break
    next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)


    # Initiate STAR detector
    orb = cv2.ORB_create(500)

    # find the keypoints with ORB
    kp, des = orb.detectAndCompute(next, None)


    # draw only keypoints location,not size and orientation
    img2 = cv2.drawKeypoints(next, kp, np.array([]),color=(0,255,0), flags=0)
    cv2.imshow('a',img2)

    countFrame += 1
    print(countFrame)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    elif k == ord('s'):
        cv2.imwrite('opticalfb.png',frame2)
        cv2.imwrite('opticalhsv.png',rgb)
    prvs = next

cap.release()
cv2.destroyAllWindows()
