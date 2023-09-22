# Recording a video

from ast import Break
from calendar import c
from tkinter import Frame
import cv2 as cv
cap= cv.VideoCapture("resources/video.mp4")


# indicator
if (cap.isOpened()==False):
    print("Error in reading video file")
    
# reading and playing

while(cap.isOpened()):
    ret,frame=cap.read()    
    if ret==True:
        cv.imshow("video",frame)
        if cv.waitKey(1) & 0xFF==ord("q"):
            break
    else:
        break
cap.release()
cap.destroyAllWindows()    