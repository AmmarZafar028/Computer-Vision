# Saving Hd recording of cam steaming

import cv2 as cv
import numpy as np

cap=cv.VideoCapture(0)

# resolution HD (1280,720)

def hd_resolutions():
    cap.set(3,1280)
    cap.set(4,720)
def sd_resolutions():
    cap.set(3,640)
    cap.set(4,480)
def fhd_resolutions():
    cap.set(3,1920)
    cap.set(4,1080)
    
hd_resolutions()
#sd_resolutions()
#fhd_resolutions()

# writing format,codec,video writer object and file output
frame_width=int(cap.get(3))
frame_height=int(cap.get(4))
out=cv.VideoWriter("resources/cam_video.avi",cv.VideoWriter_fourcc('M','J','P','G'),10,(frame_width,frame_height))


    
# Reading and Playing
while (True):
    (ret,frame)=cap.read()
    
    # to show in player
    if ret ==True:
        out.write(frame)
        cv.imshow("Video",frame)
        
        # to show with q key
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cap.destroyAllWindows()

