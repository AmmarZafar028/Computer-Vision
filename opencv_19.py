# coordinates of an image or video

# Step # 1 : Importing the libraries

import numpy as np
import cv2 as cv

# Step # 2 : Reading the image
def find_coord(event,x,y,flags,param):
    if event==cv.EVENT_LBUTTONDOWN:
        # left mouse click
        print(x,y)
        
        # How to define or print on the same image or window
        font=cv.FONT_HERSHEY_PLAIN
        cv.putText(img,str(x)+","+str(y),(x,y),font,1,(255,0,0),thickness=2)
        # Show the text on image and image itself
        cv.imshow("image",img)
        
        # for color binding
    if event==cv.EVENT_RBUTTONDOWN:
        print(x,'',y)
        
        font=cv.FONT_HERSHEY_COMPLEX
        b=img[y,x,0]
        g=img[y,x,1]
        r=img[y,x,2]
        
        cv.putText(img,str(b)+","+str(g)+","+str(r),(x,y),font,1,(0,255,0),thickness=2)
        cv.imshow("image",img)
        
#Step # 3 final function to read an display the image

if __name__=="__main__":
    img=cv.imread("resources/image.jpg",1)
    cv.imshow("image",img)
    cv.setMouseCallback("image",find_coord)
    cv.waitKey(0)
    cv.destroyAllWindows()
    
    
        