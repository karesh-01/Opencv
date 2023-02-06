import cv2 as cv

img=cv.imread("Photos/Dog.jpg")

# Averaging
average=cv.blur(img,(3,3))

# Median Blur
median=cv.medianBlur(img,7)
#cv.imshow("Median Blur",median)

# Bilateral
bilat=cv.bilateralFilter(img,5,15,15)
cv.imshow("Bilateral",bilat)

cv.waitKey(0)