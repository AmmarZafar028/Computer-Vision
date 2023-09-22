# How to draw lines, and shapes in python using opencv 
import cv2 as cv
import numpy as np

# Draw a canvas 0 is for black 
img=np.zeros((600,600)) # Black
img1=np.ones((600,600)) 

# print size
print("The size of our canvas is:",img.shape)
print(img)

# adding colors to the canvas

colored_img=np.zeros((600,600,3),np.uint8)  # Color channel addition

colored_img[:]=255,0,255  # Color complete image

colored_img[150:230,100:500]=255,0,0  # Part of the image to be colored

# adding line

cv.line(colored_img,(0,0),(600,600),(255,0,0),3) # part line
cv.line(colored_img,(0,0),(colored_img.shape[0],colored_img.shape[1]),(255,0,0),3)# cross line line

# Adding rectangle

cv.rectangle(colored_img,(50,100),(300,400),(255,255,255),3) # part rectangle
cv.rectangle(colored_img,(50,100),(300,400),(255,255,255),cv.FILLED) # Fill rectangle

# Adding circle
cv.circle(colored_img,(400,300),50,(255,100,0),5) # part circle
cv.circle(colored_img,(400,300),50,(255,100,0),cv.FILLED) # Fill circle

# Adding text
cv.putText(colored_img,"Hello World",(300,100),cv.FONT_HERSHEY_COMPLEX,1,(0,150,0),2)



#cv.imshow("Black",img)
#cv.imshow("White",img1)
cv.imshow("Colored",colored_img)
cv.waitKey(0)
cv.destroyAllWindows()