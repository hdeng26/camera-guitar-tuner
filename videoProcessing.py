import cv2
import numpy as np
import math
import time
import periodDetection_orange

cap = cv2.VideoCapture("EADGBE.mp4")

ret, frame1 = cap.read()
prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[...,1] = 255
img_redline = cv2.imread('test2.jpg')

while(1):
    ret, frame2 = cap.read()
    if ret is False:
        break
    #next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
    output = periodDetection_orange.imageProcess(frame2,img_redline)
    cv2.imshow("output", output)
    #prvs = next
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
