import numpy as np
import cv2
from matplotlib import pyplot as plt
import time

cap = cv2.VideoCapture('EADGBE.mp4')
ret1, frame1 = cap.read()
prvs = cv2.GaussianBlur(cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY),(5,5),0)

count = 0
width = int(cap.get(3))
height = int(cap.get(4))

while(cap.isOpened()):
    # Capture frame-by-frame
    ret2, frame2 = cap.read()
    if not ret1 or not ret2:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    next = cv2.GaussianBlur(cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY),(5,5),0)
    flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
    mag[mag < (mag.mean())] = 0
    mag[mag > 0] = 255
    #mag = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
    mag = np.uint8(mag)

    #_, mag = cv2.threshold(mag, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    time.sleep(0.1)

    cv2.imshow('mag', mag)
    '''
    newFrame = np.zeros_like(baseOutput)
    for y in range(0, baseOutput.shape[0]):
        for x in range(0, baseOutput.shape[1]):
            if y+int(flow[y][x][1]) < baseOutput.shape[0] and x+int(flow[y][x][0]) < baseOutput.shape[1]:
                newFrame[y+int(flow[y][x][1])][x+int(flow[y][x][0])] = baseOutput[y][x]

    count += 1
    print(count)

    if count % 10 == 0:
        dynamic_style = processFrame(next, outputIntensity)
        for y in range(0, newFrame.shape[0]):
            for x in range(0, newFrame.shape[1]):
                if mag[y][x] > 0:
                    newFrame[y][x] = dynamic_style[y][x]
                    baseOutput[y][x] = dynamic_style[y][x]

    cv2.imshow('frameNew', newFrame)
    '''

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    prvs = next

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

