import cv2 as cv
import numpy as np

image1 = cv.imread('image/isro.jpeg')
image2 = cv.imread('image/isro2.jpeg')

# add = cv.addWeighted(image1, 0.5, image2, 0.5, 0)
sub = cv.subtract(image1, image2)

# cv.imshow("Added Image", add)
cv.imshow("Subtracted Image", sub)

if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()