import cv2
import numpy as np

img = cv2.imread('test2.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,30,150,apertureSize = 3)

lines = cv2.HoughLines(edges,1,np.pi/180,130)


def slice_into_string(image,height_cocrdinate):
    string_img = image[height_cocrdinate-10:height_cocrdinate+10, 0:image.shape[0]]
    return string_img


def rotate_image(image, angle):
  #image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D((0, 0), angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result


for index, line in enumerate(lines):
    rho = line[0][0]
    theta = line[0][1]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),1)
    img_index = str(index)
    calibration_img = rotate_image(img, theta*180/np.pi-90)
    cv2.imshow('calibration_img',calibration_img)
    cv2.waitKey(0)
    sliced_string = slice_into_string(calibration_img, int(rho))
    cv2.imwrite('string_'+img_index+'.jpg', sliced_string)






print(lines)
print('lines',len(lines))
cv2.imwrite('houghlines6.jpg',img)
