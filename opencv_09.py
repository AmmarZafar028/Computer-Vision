 # How to capture a webcam inside python
 
# Import Libraries
from tkinter import Frame
import cv2 as cv
import numpy as np

# Step # 2 Read the frames from camera
cap=cv.VideoCapture(0) # webcam no.1

 # read until the end 
# step # 3 Display frame by frame
while(cap.isOpened()):
    
    # capture frame by frame
    ret,frame=cap.read()
    if ret==True:
        
        # To display frame
        cv.imshow("Frame",frame)
        
        # to show with q key
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    
# step # 4 release or close windows
    cap.release()
    cv.destroyAllWindows()