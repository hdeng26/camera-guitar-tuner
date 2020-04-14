import cv2
import numpy as np
import math
import time
import periodDetection_orange

cap = cv2.VideoCapture("sampleTest.mp4")

STANDARD = [2.7753623195652173, 2.1954913645508416, 1.8611955802229712, 1.3333333570557402, 1.1422602269713267, 0.9340389771162532]
STRING_DIS = 46
#ret, frame1 = cap.read()
#prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
#hsv = np.zeros_like(frame1)
#hsv[...,1] = 255
img_redline = cv2.imread('test2.jpg')
waveLengthCollection = [[],[],[],[],[],[]]
while(1):
    ret, frame2 = cap.read()
    if ret is False:
        break
    #next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
    output, waveArray = periodDetection_orange.imageProcess(frame2,img_redline)

    for i in range(len(waveArray)):
        if waveArray[i] is not 0:
            if waveArray[i]/STRING_DIS > STANDARD[i]+0.2:
                print("string No.", i, "is too high\n")
            elif waveArray[i]/STRING_DIS < STANDARD[i]-0.2:
                print("string No.", i, "is too low\n")
            else:
                print("string No.", i, "is good\n")

    cv2.imshow("output", output)
    print("***********frame************")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
''' 
print(waveLengthCollection)
for i in range(len(waveLengthCollection)):
    print("average for string", i, np.mean(waveLengthCollection[i]))
'''
cap.release()
cv2.destroyAllWindows()
