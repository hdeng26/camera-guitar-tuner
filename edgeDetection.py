import numpy as np
import cv2

       # Read the main image

inputImage = cv2.imread("test1.jpg")


inputImageGray = cv2.cvtColor(inputImage, cv2.COLOR_BGR2GRAY)

       # Line Detection

edges = cv2.Canny(inputImageGray,100,200,apertureSize = 3)

minLineLength = 500 
maxLineGap = 5 

lines = cv2.HoughLinesP(edges,1,np.pi/180,90,minLineLength,maxLineGap)

for x in range(0, len(lines)):
    for x1,y1,x2,y2 in lines[x]:
        cv2.line(inputImage,(x1,y1),(x2,y2),(0,128,0),2)

#cv2.putText(inputImage,"Tracks Detected", (500,250), font, 0.5, 255)

# Show result
cv2.imshow("Trolley_Problem_Result", inputImage)
