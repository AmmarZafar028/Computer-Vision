# writing videos from cam
import cv2 as cv
cap= cv.VideoCapture("resources/video.mp4")

# writing format,codec,video writer object and file output
frame_width=int(cap.get(3))
frame_height=int(cap.get(4))
out=cv.VideoWriter("resources/Out_video.avi",cv.VideoWriter_fourcc('M','J','P','G'),10,(frame_width,frame_height),isColor=False)


    
# Reading and Playing
while (True):
    (ret,frame)=cap.read()
    gray_frame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    
    # to show in player
    if ret ==True:
        out.write(gray_frame)
        cv.imshow("Video",gray_frame)
        
        # to show with q key
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cap.destroyAllWindows()
    