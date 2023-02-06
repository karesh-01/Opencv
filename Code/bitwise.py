import cv2 as cv
import numpy as np

blank=np.zeros((500,500),dtype='uint8')

rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle=cv.circle(blank.copy(),(200,200),200,255,-1)

# Bitwise and
bitand=cv.bitwise_and(rectangle,circle)

# Bitwise or
bitor=cv.bitwise_or(rectangle,circle)

# Bitwise xor
bitxor=cv.bitwise_xor(rectangle,circle)

# Bitwise not
bitnot=cv.bitwise_not(rectangle)

cv.imshow("and",bitand)
cv.imshow("or",bitor)
cv.imshow("not",bitnot)
cv.imshow("xor",bitxor)

cv.waitKey(0)

