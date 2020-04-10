import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv2.imread('test1.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('a3.png',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.95
loc = np.where( res >= threshold)
print(loc)
location = [[loc[0][0]],[loc[1][0]]]

for i in range(1,len(loc[1])):
    if loc[1][i] - loc[1][i-1] > 5:
        location[0].append(loc[0][i])
        location[1].append(loc[1][i])


print(location)

wavelenth = 0
for i in range(1,len(location[1])):
    lenth = np.sqrt((location[1][i]-location[1][i-1])**2 + (location[0][i]-location[0][i-1])**2)
    print(lenth)
    wavelenth += lenth

    

wavelenth /= (len(location[1]) - 1)
print(wavelenth)

for pt in zip(*location[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

  

cv2.imshow('res',img_rgb)
cv2.waitKey(0)
# todo: use the center of red line to create a may be 50*50 area and when red line disappered, use this function to match same area
