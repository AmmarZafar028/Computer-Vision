# split your video into frames

import cv2 as cv

cap=cv.VideoCapture("resources/video.mp4")

frameNr=0

while True:
    success,frame=cap.read()
    if success:
        cv.imwrite(f"resources/frames/frame_{frameNr}.jpg",frame)
    else:
        break
    frameNr=frameNr+1
cap.release()