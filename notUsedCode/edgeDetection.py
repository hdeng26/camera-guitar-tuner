import numpy as np
import cv2
import sys
import math

np.set_printoptions(threshold=sys.maxsize)
       # Read the main image

def getRedline(input):
    img = cv2.cvtColor(input,cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(img, 30, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 130)
    print(lines)
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


image = "test1.jpg"
imgRed = cv2.imread("noTouching.jpg")
red = getRedline(imgRed)
img = cv2.imread(image)
img2 = cv2.imread(image)
edge = cv2.Canny(img,100,200)
inputImage = cv2.imread(image, 0)
blur = cv2.GaussianBlur(inputImage,(5,5),0)
sobelx = cv2.Sobel(blur,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(blur,cv2.CV_64F,0,1,ksize=5)


theta = np.arctan2(np.float32(sobely), np.float32(sobelx))
cv2.imshow("output", red)

blur = 255*(abs(theta/np.pi))
img2[edge == 0] = [0,0,0]
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if edge[i][j] == 255 and red[i][j][2] == 255:
            print(blur[i][j], j, i)
            img2[i][j] = [0,0,255]
'''
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if edge[i][j] == 255: # and blur[i][j]<160 and blur[i][j]>150:
            
            img2[i][j] = [blur[i][j], 128, 255 - blur[i][j]]
        if edge[i][j] == 255 and blur[i][j]<170+5 and blur[i][j]>170-5:
            img[i][j] = [255, 255, 0]

#print(blur, blur.max(), blur.min())
cv2.imshow("output", img2)
cv2.imshow("point", img)
#print(edge)
'''
cv2.imshow("output", red)
