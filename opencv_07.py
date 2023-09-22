# converting video to black and white

import cv2 as cv
cap= cv.VideoCapture("resources/video.mp4")


    
# Reading and Playing
while (True):
    (ret,frame)=cap.read()
    gray_frame=cv.cvtColor(frame,cv.cvtColor_BGR2GRAY)
    (thresh,binary)=cv.threshold(gray_frame,127,255,cv.THRESH_BINARY)
    
    # to show in player
    if ret ==True:
        cv.imshow("Video",binary)
        
        # to show with q key
        if cv.waitkey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cap.destroyAllWindows()
    