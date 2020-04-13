import numpy as np
import cv2
import sys
np.set_printoptions(threshold=sys.maxsize)
       # Read the main image
image = "test1.jpg"
img = cv2.imread(image)
img2 = cv2.imread(image)
edge = cv2.Canny(img,100,200)
inputImage = cv2.imread(image, 0)
blur = cv2.GaussianBlur(inputImage,(5,5),0)
sobelx = cv2.Sobel(blur,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(blur,cv2.CV_64F,0,1,ksize=5)
'''
abs_grad_x = cv2.convertScaleAbs(sobelx)
abs_grad_y = cv2.convertScaleAbs(sobely)
grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
cv2.imshow("grad", grad)'''

theta = np.arctan2(np.float32(sobely), np.float32(sobelx))
'''
img[...,0] = 255*(abs(theta/np.pi))
img[...,2] = 0
img[...,1] = cv2.normalize(grad,None,0,255,cv2.NORM_MINMAX)'''

blur = 255*(abs(theta/np.pi))
img2[edge == 0] = [0,0,0]
#img[(edge[blur>127],edge[blur>127]).all] = [255,255,0]
#img.all(edge[blur>127],edge[blur>127]) = [255,255,0]
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if edge[i][j] == 255: # and blur[i][j]<160 and blur[i][j]>150:
            
            img2[i][j] = [blur[i][j], 128, 255 - blur[i][j] ]
        if edge[i][j] == 255 and blur[i][j]<170+5 and blur[i][j]>170-5:
            img[i][j] = [255, 255, 0]

#print(blur, blur.max(), blur.min())
cv2.imshow("output", img2)
cv2.imshow("point", img)
#print(edge)
