import cv2
import numpy as np
cap = cv2.VideoCapture("sampleTest.mp4")

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
    gray = np.float32(next)
    dst = cv2.cornerHarris(gray,2,3,0.1)
    dst = cv2.dilate(dst,None)
    frame2[dst>0.01*dst.max()]=[0,0,255]
    cv2.imshow('dst',frame2)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    elif k == ord('s'):
        cv2.imwrite('opticalfb.png',frame2)
        cv2.imwrite('opticalhsv.png',rgb)
    #prvs = next

cap.release()
cv2.destroyAllWindows()
