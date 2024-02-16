import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while 1:
    
    _, frame = cap.read() # grab each frame

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) # change background to hsv
    
    lower_blue = np.array([110,50,50]) # range of blue color in hsv
    upper_blue = np.array([130,255,255])

    mask = cv.inRange(hsv, lower_blue, upper_blue) # threshold the hsv image to get only blue colors
    
    res = cv.bitwise_and(frame, frame, mask=mask) # bitwise-and mask and original image

    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)

    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()