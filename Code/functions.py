import cv2 as cv

img = cv.imread("Photos/Dog.jpg")

# BGR to Grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow("Gray",gray)

# Blur
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
#cv.imshow("Blur",blur)

# Edge Cascade
canny=cv.Canny(img,125,175)
#cv.imshow("Canny",canny)

# Dilating
dilate=cv.dilate(canny,(3,3),iterations=3)
#cv.imshow("Dilate",dilate)

# Eroding
eroded = cv.erode(dilate,(3,3),iterations=3)
#cv.imshow("Eroded",eroded)

# Resize
resized=cv.resize(img,(600,500))
#cv.imshow("Resized",resized)

# Cropping
cropped=img[50:200, 200:400]
cv.imshow("Cropped",cropped)

cv.waitKey(0)
