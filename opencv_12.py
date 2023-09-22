# setting of camera or video

import cv2 as cv
import numpy as np
cap=cv.VideoCapture(0)

cap.set(10,100) # 100 is the key to success
cap.set(3,640) # width key
cap.set(4,480) # height key

while(True):
    ret,frame=cap.read()
    if ret==True:
        cv.imshow("frame",frame)
        if cv.waitKey(1) & 0xFF==ord("q"):
            break
    else:
        break
        
cap.release()
cap.destroyAllWindows