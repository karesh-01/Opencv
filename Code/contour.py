import cv2 as cv
import numpy as np

img = cv.imread("Photos/Dog.jpg")
blank=np.zeros(img.shape[:2],dtype='uint8')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
canny=cv.Canny(img,125,175)
#cv.imshow("Canny",canny)

contours,hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(len(contours))

ret,thresh=cv.threshold(gray,125,125,cv.THRESH_BINARY)
cv.drawContours(blank,contours,-1,(0,0,255),2)
cv.imshow("Contours",thresh)

cv.waitKey(0)