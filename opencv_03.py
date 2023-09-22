# Gray scale conversion

# Import library
import cv2 as cv
from cv2 import cvtColor

img=cv.imread("resources/image.jpg")

# Conversion
gray_img=cvtColor(img,cv.COLOR_BGR2GRAY)

# Display code
cv.imshow("1st image",img)
cv.imshow("Gray Image",gray_img)

# Delay code
cv.waitKey(0)
cv.destroyAllWindows()