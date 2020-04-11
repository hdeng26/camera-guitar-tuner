import cv2
import numpy as np
import math
import time

from wavelenth import getResultAndWavelenth as getWL

COLOR = [(0,0,255), (0,255,0), (255,0,0), (0,255,255), (255,0,255), (255,255,0)]

def getRedline(input):
    img = cv2.cvtColor(input,cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(img, 30, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 130)
    imgCopy = input.copy()
    imgCopy.fill(0)
    angles = []
    liney = []
    linesCopy = []
    if lines is not None:
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
            if angle<5 and angle>-5:
                cv2.line(imgCopy, (x1, y1), (x2, y2), (0, 0, 255), 1)
                angles.append(angle)

    return imgCopy
    

def getTemplates(input, redLine):
    boxRange = 15
    boxPos = input.copy()
    curRedline = getRedline(input)
    curRedline = cv2.cvtColor(curRedline,cv2.COLOR_BGR2GRAY)
    templates = []
    centerLine = int(redLine.shape[1]/2)
    string = cv2.cvtColor(redLine, cv2.COLOR_BGR2GRAY)
    for i in range(redLine.shape[0]):
        if string[i][centerLine] != 0:
            curBox = curRedline[i-int(boxRange*1.2):i+int(boxRange*1.2), centerLine-boxRange*2:centerLine+boxRange*2]
            if curBox[curBox>0].any():
                #print("curLine contains straight line")
                continue
            
            templates.append(input[i-int(boxRange*1.2):i+int(boxRange*1.2), centerLine-boxRange*2:centerLine+boxRange*2])
            boxPos[i-boxRange,centerLine] = [255, 255, 255]
    #cv2.imshow("box", boxPos)
    return templates

def matchTemplate(input, template, color):
    img_gray = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.90
    loc = np.where( res >= threshold)
    
    location,wavelenth = getWL(loc)
    for pt in zip(*location[::-1]):
        cv2.rectangle(input, pt, (pt[0] + w, pt[1] + h), color, 2)
    return input
    
def imageProcess(frame, redlineImg):
    #img_redline = cv2.imread('test2.jpg')
    redline = getRedline(redlineImg)
    #cv2.imshow('HoughLine', redline)

    #img_rgb = cv2.imread('test3.jpg')
    tempList = getTemplates(frame, redline)
        
    output = frame.copy()
    for i in range(len(tempList)):
        output = matchTemplate(frame, tempList[i], COLOR[i%6])
    return output
    #cv2.imshow('res',output)
    #cv2.waitKey(0)
