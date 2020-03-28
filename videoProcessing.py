import cv2
import numpy as np
import math

cap = cv2.VideoCapture("sample.mp4")

ret, frame1 = cap.read()
prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[...,1] = 255

while(1):
    ret, frame2 = cap.read()
    next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)

    '''flow = cv2.calcOpticalFlowFarneback(prvs,next, None, 0.5, 5, 5, 3, 5, 1.1, 0)

    mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
    hsv[...,0] = ang*180/np.pi/2
    hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
    rgb = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
    canny = np.uint8(np.absolute(frame2))
    canny[rgb == 0] = 0
    canny[rgb > 0] = 255
    cv2.imshow('frame2',canny)'''
    # gray = np.float32(next)
    edges = cv2.Canny(next, 30, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 130)
    imgCopy = frame2.copy()
    angles = []

    if lines is not None:
        for line in lines:
            rho = line[0][0]
            theta = line[0][1]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
            if angle<5 and angle>-5:
                cv2.line(imgCopy, (x1, y1), (x2, y2), (0, 0, 255), 1)
                angles.append(angle)
    print(angles)
    cv2.imshow('HoughLine', imgCopy)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    elif k == ord('s'):
        cv2.imwrite('opticalfb.png',frame2)
        cv2.imwrite('opticalhsv.png',rgb)
    prvs = next

cap.release()
cv2.destroyAllWindows()
