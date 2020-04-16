import cv2
import numpy as np
import math
import time
import periodDetection

cap = cv2.VideoCapture("sampleTest.mp4")
'''standard wavelength for 6 string in tone E A D G B E'''
STANDARD = [2.7753623195652173, 2.1954913645508416, 1.8611955802229712, 1.3333333570557402, 1.1422602269713267, 0.9340389771162532]
STRING_DIS = 46

img_redline = cv2.imread('test2.jpg')
waveLengthCollection = [[],[],[],[],[],[]]
while(1):
    ret, frame = cap.read()
    if ret is False:
        break
    # get wavelength from current string wave
    output, waveArray = periodDetection_orange.imageProcess(frame,img_redline)

    # output realtime result
    for i in range(len(waveArray)):
        if waveArray[i] is not 0:
            if waveArray[i]/STRING_DIS > STANDARD[i]+0.2:
                print("string No.", i, "is too high\n")
            elif waveArray[i]/STRING_DIS < STANDARD[i]-0.2:
                print("string No.", i, "is too low\n")
            else:
                print("string No.", i, "is good\n")

    cv2.imshow("output", output)
    # turn to next frame
    print("***********frame************")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
