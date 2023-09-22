# Basic functions or manipulation in open cv

import cv2 as cv
import numpy as np
from cv2 import blur
img=cv.imread("resources/image.jpg")

# resize
resized_img=cv.resize(img,(450,250))

# gray
gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# blur
blur_img=cv.GaussianBlur(img,(7,7),0)

# edge detection
edge_img=cv.Canny(img,53,53)

# thickness of lines
mat_kernel=np.ones((3,3),np.uint8)
dilated_img=cv.dilate(edge_img,(mat_kernel),iterations=1)

# Make thinner outline
ero_img=cv.erode(dilated_img,mat_kernel,iterations=1)

# We will use numpy library not open cv

print("The size of our image is:",img.shape)
cropped_img=img[0:500,150:400]










cv.imshow("Original",img)
cv.imshow("Resized",resized_img)
cv.imshow("Gray",gray_img)
cv.imshow("Blur",blur_img)
cv.imshow("Edge",edge_img)
cv.imshow("Dilated",dilated_img)
cv.imshow("Erosion",ero_img)
cv.imshow("Cropped",cropped_img)
cv.waitKey(0)
cv.destroyAllWindows()
