# Face and Eyes detection in images

# Import the open cv library
import cv2 as cv

# load the cascade
face_cascade = cv.CascadeClassifier("resources/haarcascade_frontalface_default.xml")
eye_cascade = cv.CascadeClassifier("resources/haarcascade_eye.xml")

# Read in the image
img = cv.imread("resources/messi_image.jpg")
Gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(Gray_img,scaleFactor=1.05,minNeighbors=5)

# Print the number of faces found in the image
print("Face found: ",len(faces))
print("The image height,width and channels are: ",img.shape)
print("The coordinates of the faces are: ",faces)

# Draw a rectangle around the face and eyes
for (x,y,w,h) in faces:
    img = cv.rectangle(img,(x,y),(x+w,y+h),(179,255,0),3)
    roi_face = img[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_face)
    for (ex,ey,ew,eh) in eyes:
        cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        
# Resize the image
img = cv.resize(img,(900,700))
print(img.shape)

font = cv.FONT_HERSHEY_SIMPLEX
text = cv.putText(img,"Face and eyes detection",(10,50),font,1,(0,0,255),2,cv.LINE_AA)
        
# Display the image
cv.imshow("image1",img)
cv.waitKey(0)
cv.destroyAllWindows()






