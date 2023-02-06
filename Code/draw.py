import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3), dtype='uint8')
# cv.imshow("Blank",blank)

# blank[200:300, 300:400]=0,255,0
# cv.imshow("Color",blank)

# cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=cv.FILLED)
# cv.circle(blank,(250,250),40,(0,0,255),thickness=-1)
# cv.line(blank,(0,0),(250,250),(255,255,255),thickness=3)
cv.putText(blank,"Hey! Karesh here!",(0,255),cv.FONT_HERSHEY_SCRIPT_COMPLEX,1.0, (0,255,0),3)
cv.imshow("Blank",blank)

cv.waitKey(0)