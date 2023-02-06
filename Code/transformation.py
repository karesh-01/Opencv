import cv2 as cv
import numpy as np

img=cv.imread("Photos/Dog.jpg")

# Translate
# cv.imshow("Original",img)
# def translate(img,x,y):
#     transMat=np.float32([[1,0,x],[0,1,y]])
#     dimen=(img.shape[1],img.shape[0])
#     return cv.warpAffine(img,transMat,dimen)
# trans=translate(img,100,100)
# cv.imshow("Translate",trans)

# Rotation
# def rotate(img,angle,rotpt=None):
#     (height,width)=img.shape[:2]
#     if rotpt is None:
#         rotpt=(width//2,height//2)
#     rotmat=cv.getRotationMatrix2D(rotpt,angle,1.0)
#     dimen=(width,height)
#     return cv.warpAffine(img,rotmat,dimen)
# rot=rotate(img,45)
# cv.imshow("Rotate",rot)

# Flip
flip=cv.flip(img,0)
cv.imshow("Flip",flip)

cv.waitKey(0)