import cv2
import numpy as np
from matplotlib import pyplot as plt
import math
import time

COLOR = [(0,0,255), (0,255,0), (255,0,0), (0,255,255), (255,0,255), (255,255,0)]

def redline(input):
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
                        print(otherLine, liney)
                        liney.remove(otherLine)
        print(liney)
        for line in range(len(lines)):
            if line in liney:
                linesCopy.append(lines[line])
        print(linesCopy)
            
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
    print(angles)
    return imgCopy
    

def getTemplates(input, redLine):
    templates = []
    centerLine = int(redLine.shape[1]/2)
    string = cv2.cvtColor(redLine, cv2.COLOR_BGR2GRAY)
    for i in range(redLine.shape[0]):
        if string[i][centerLine] != 0:
            templates.append(input[i-15:i+15, centerLine-30:centerLine+30])
            #print(i)
    return templates
            

def matchTemplate(input, template, color):
    img_gray = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.90
    loc = np.where( res >= threshold)

    #import wavelenth.py, then and get optimized matching result and wavelenth
    # location,wavelenth = getResultAndWavelenth(matches)

    #modify for pt in zip(*loc[::-1]):    to    for pt in zip(*location[::-1]):
    for pt in zip(*loc[::-1]):
        cv2.rectangle(input, pt, (pt[0] + w, pt[1] + h), color, 2)
    return input
    

img_redline = cv2.imread('test2.jpg')
redline = redline(img_redline)
cv2.imshow('HoughLine', redline)



img_rgb = cv2.imread('test1.jpg')
tempList = getTemplates(img_rgb, redline)



#template = cv2.imread('a3.png',0)
#outputTemplate = matchTemplate(img_rgb, template, COLOR[0])

for i in range(len(tempList)):
    #print(tempList[i])
    output = matchTemplate(img_rgb, tempList[i], COLOR[i%6])

cv2.imshow('res',output)
cv2.waitKey(0)

# todo: use the center of red line to create a may be 50*50 area and when red line disappered, use this function to match same area
