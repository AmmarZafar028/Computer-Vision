# Image saving an image writing images

import cv2 as cv
from cv2 import imshow
from cv2 import imwrite
img=cv.imread("resources/image.jpg")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
(thresh,binary)=cv.threshold(gray,127,255,cv.THRESH_BINARY)

binary=cv.resize(binary,(500,700))


imwrite("resources/image_gray.jpg",gray)
imwrite("resources/image_bw.jpg",binary)

#cv.waitKey(0)
#cv.destroyAllWindows()