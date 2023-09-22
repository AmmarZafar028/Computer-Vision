# face detection in images

import cv2 as cv

face_cascade=cv.CascadeClassifier("resources/haarcascade_frontalface_default.xml")


img=cv.imread("resources/Ammar.jpg")

Gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(Gray_img,scaleFactor=1.05,minNeighbors=5)

# draw a rectangle around the face

for (x,y,w,h) in faces:
    img=cv.rectangle(img,(x,y),(x+w,y+h),(179,255,0),3)



img=cv.resize(img,(500,500))
print(img.shape)

cv.imshow("Ammar",img)
cv.waitKey(0)
cv.destroyAllWindows()