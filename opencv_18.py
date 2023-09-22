# How to change the perspective of an image using opencv

import cv2 as cv
import numpy as np

image=cv.imread("resources/warp.jpg")
print(image.shape)

# defining points
point1=np.float32([[111,219],[287,188],[154,482],[352,440]])

width,height=448,853
point2=np.float32([[0,0],[800,0],[0,height],[width,height]])

matrix=cv.getPerspectiveTransform(point1,point2)
out_img=cv.warpPerspective(image,matrix,(width,height))

cv.imshow("Original",image)
cv.imshow("transformed",out_img)
cv.imwrite("resources/warp_perspective.jpg",out_img)
cv.waitKey(0)
cv.destroyAllWindows()
