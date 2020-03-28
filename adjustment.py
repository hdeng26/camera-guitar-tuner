import cv2
import numpy as np
import math

image = cv2.imread('test2.png')
cv2.imshow('image', image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 30, 150, apertureSize=3)
cv2.imshow('edges', edges)
lines = cv2.HoughLines(edges, 1, np.pi / 180, 180)

imgCopy = image.copy()
angles = []

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
    cv2.line(imgCopy, (x1, y1), (x2, y2), (0, 0, 255), 1)
    angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
    angles.append(angle)

print(angles)
cv2.imwrite('HoughLine.png', imgCopy)
cv2.imshow('HoughLine', imgCopy)
cv2.waitKey(0)
