## Reading an image and displaying it

import cv2 as cv

img=cv.imread("resources/image.jpg")
img1=cv.resize(img,(500,700))     # size of the new image


cv.imshow("1st image",img)
cv.imshow("2nd image",img1)
cv.waitKey(0)                # Delay in milliseconds
cv.destroyAllWindows()             # closes All windows