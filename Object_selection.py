# How to detect specific color inside python using opencv

# Step # 1 : Importing the libraries
import cv2 as cv
import numpy as np

img=cv.imread("resources/image.jpg")

# convert in hsv(hue, saturation ,color)
hsv_img=cv.cvtColor(img,cv.COLOR_BGR2HSV)

# sliders 

def slider():
    pass
path="resources/image.jpg"
    
cv.namedWindow("Bars")
cv.resizeWindow("Bars",640,240)

cv.createTrackbar("Hue Min","Bars",0,179,slider)
cv.createTrackbar("Hue Max","Bars",19,179,slider)
cv.createTrackbar("Sat Min","Bars",110,255,slider)
cv.createTrackbar("Sat Max","Bars",240,255,slider)
cv.createTrackbar("Val Min","Bars",153,255,slider)
cv.createTrackbar("Val Max","Bars",255,255,slider)

img=cv.imread(path)
hsv_img=cv.cvtColor(img,cv.COLOR_BGR2HSV)

#hue_min=cv.getTrackbarPos("Hue Min","Bars")
#print(hue_min)





while True:
    img=cv.imread(path)
    hsv_img=cv.cvtColor(img,cv.COLOR_BGR2HSV)
    hue_min=cv.getTrackbarPos("Hue Min","Bars")
    hue_max=cv.getTrackbarPos("Hue Max","Bars")
    sat_min=cv.getTrackbarPos("Sat Min","Bars")
    sat_max=cv.getTrackbarPos("Sat Max","Bars")
    val_min=cv.getTrackbarPos("Val Min","Bars")
    val_max=cv.getTrackbarPos("Val Max","Bars")
    print(hue_min,hue_max,sat_min,sat_max,val_min,val_max)
    
    # to see these changes inside an image
    lower=np.array([hue_min,sat_min,val_min])
    upper=np.array([hue_max,sat_max,val_max])
    mask_img=cv.inRange(hsv_img,lower,upper)
    out_img=cv.bitwise_and(img,img,mask=mask_img)
    
    cv.imshow("Origial",img)
    cv.imshow("HSV",hsv_img)
    cv.imshow("Mask",mask_img)
    cv.imshow("Final Output",out_img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()

    



