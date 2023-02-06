import cv2 as cv
import numpy as np


img=cv.imread("Photos/Dog.jpg")
blank=np.zeros(img.shape[:2],dtype='uint8')

# BGR to HSV
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
#cv.imshow("HSV",hsv)

# BGR to LAB
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
#cv.imshow("Lab",lab)

# Color Channels
b,g,r=cv.split(img)
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged=cv.merge([b,g,r])
blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])

cv.imshow("Blue",blue)
cv.imshow("Green",green)
cv.imshow("Red",red)

cv.waitKey(0)
