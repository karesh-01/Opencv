import cv2 as cv

# Reading image

# img = cv.imread("Photos/Dog.jpg")
# cv.imshow("Dog",img)
# cv.waitKey(0)


#Reading video and rescaling

# def rescaleFrame(frame, scale=0.75):
#     width=int(frame.shape[1]*scale)
#     height=int(frame.shape[0]*scale)
#     dimensions=(width,height)
#     return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture(0)

while True:
    isTrue, frame=capture.read()
   # resizeframe=rescaleFrame(frame)
    cv.imshow("Original",frame)
   # cv.imshow("Resized",resizeframe)
    frame.set()
    if cv.waitKey(20) & 0xFF==ord('k'):
        break
capture.release()
cv.destroyAllWindows()