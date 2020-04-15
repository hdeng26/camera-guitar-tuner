import cv2
import numpy as np
import math
import time

from wavelenth import getResultAndWavelenth as getWL
wavelengthStandard = [127.6666667, 100.99260276933872, 85.61499669025667, 61.33333442456405, 52.54397044068103, 42.965792947347644]
STANDARD = [2.7753623195652173, 2.1954913645508416, 1.8611955802229712, 1.3333333570557402, 1.1422602269713267, 0.9340389771162532] #STANDARD = wavelengthStandard/STRING_DIS
STRING_DIS = 46

COLOR = [(0,0,255), (0,255,0), (255,0,0), (0,255,255), (255,0,255), (255,255,0)]

def getRedline(input):
    '''get Hough line based on string'''
    img = cv2.cvtColor(input,cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(img, 30, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 130)
    imgCopy = input.copy()
    imgCopy.fill(0)
    angles = []
    liney = []
    linesCopy = []
    if lines is not None:
        '''lineCopy removes duplicate element from lines'''
        for i in range(len(lines)):
            liney.append(i)
            
        for line in liney:
            for otherLine in range(len(lines)):
                if otherLine in liney:
                    if abs(lines[line][0][0] - lines[otherLine][0][0]) < 15.0 and abs(lines[line][0][0] - lines[otherLine][0][0]) > 0 :
                        liney.remove(otherLine)
                        
        for line in range(len(lines)):
            if line in liney:
                linesCopy.append(lines[line])

        for line in linesCopy:
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
            '''set threshold for angle of hough lines'''
            if angle<5 and angle>-5:
                cv2.line(imgCopy, (x1, y1), (x2, y2), (0, 0, 255), 1)
                angles.append(angle)

    return imgCopy
    

def getTemplates(input, redLine):
    '''get templates based on the center of hough line position'''
    boxRange = 20
    boxPos = input.copy()
    curRedline = getRedline(input)

    curRedline = cv2.cvtColor(curRedline,cv2.COLOR_BGR2GRAY)
    templates = []
    centerLine = int(redLine.shape[1]/2)
    string = cv2.cvtColor(redLine, cv2.COLOR_BGR2GRAY)
    count = 0
    order = []
    for i in range(redLine.shape[0]):
        if string[i][centerLine] != 0:
            curBox = curRedline[i-boxRange:i+boxRange, centerLine-boxRange:centerLine+boxRange]
            if curBox[curBox>0].any():
                '''curLine contains straight line and we only want curve template'''
                count += 1
                continue
            order.append(count)
            templates.append(input[i-boxRange:i+boxRange, centerLine-boxRange:centerLine+boxRange])
            boxPos[i-boxRange,centerLine] = [255, 255, 255]
            count += 1

    return templates, order

def matchTemplate(input, template, color):
    '''match the same curve templates and color matched templates in same color'''
    img_gray = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where( res >= threshold)

    if len(loc[0]) == 0 or len(loc[1]) == 0:
        cv2.imshow("666",input)
        return input
    '''calculate the wavelength in matched templates'''
    location,wavelenth = getWL(loc)
    for pt in zip(*location[::-1]):
        cv2.rectangle(input, pt, (pt[0] + w, pt[1] + h), color, 2)
    return input, wavelenth
    


def get6lines(frame, redlineImg):
    '''cut frame into six parts which contains 6 guitar strings'''
    centerLine = int(redlineImg.shape[1]/2)
    boxRange = int(STRING_DIS/2)
    string = cv2.cvtColor(redlineImg, cv2.COLOR_BGR2GRAY)

    strings = []
    for i in range(redlineImg.shape[0]):
        if string[i][centerLine] != 0:

            stringBox = frame[i-boxRange:i+boxRange, 0:redlineImg.shape[1]]
            strings.append(stringBox)
    return strings

def imageProcess(frame, redlineImg):
    '''process current frame and output current 6 wavelengths'''
    redline = getRedline(redlineImg)

    tempList, order = getTemplates(frame, redline)

    stringList = get6lines(frame, redline)

    waveLengthArray = [0, 0, 0, 0, 0, 0]
    output = np.copy(frame)
    count = 0

    for i in range(6):
        if len(order)>count and order[count] == i:
            newOutput, currentWavelength = matchTemplate(stringList[i], tempList[count], COLOR[i%6])
            waveLengthArray[i] = currentWavelength
            count += 1
        else:
            newOutput = stringList[i]
        output = np.vstack((output, newOutput))
        
    return output, waveLengthArray


