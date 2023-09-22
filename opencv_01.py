## Reading an image and displaying it
# import library

import cv2 as cv

img=cv.imread("resources/image.jpg")


cv.imshow("1st image",img)
cv.waitKey(0)
cv.destroyAllWindows()