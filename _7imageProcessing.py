import cv2 as cv
import numpy as np

path = r'F:\OpenCV\image\geeks.png'  ## path of image

image = cv.imread(path)  ## Reading an image in default mode

window_name = 'Image'  ## window name in which image is displayed


kernel = np.ones((5, 5), np.uint8)  ## creating kernel



# ### Syntax: cv2.erode(src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]])
# image = cv.erode(image, kernel)  ## using erode method
# cv.imshow(window_name, image)



### Gaussian Blur
# Gaussian = cv.GaussianBlur(image, (7, 7), 0)  
# cv.imshow("Gaussian Blurring", Gaussian)

# ### Median Blur
# median = cv.medianBlur(image, 5)
# cv.imshow("Median Blurring", median)
 
# ### Bilateral Blur
# bilateral = cv.bilateralFilter(image, 9, 75, 75)
# cv.imshow("Bilateral Blurring", bilateral)



### Syntax: cv2.copyMakeBorder(src, top, bottom, left, right, borderType, value)
# image = cv.copyMakeBorder(image, 10, 10, 10, 10, cv.BORDER_CONSTANT, None, value=0)
image = cv.copyMakeBorder(image, 100, 100, 50, 50, cv.BORDER_REFLECT) 

cv.imshow(window_name, image)



# cv.waitKey(0)
if cv.waitKey(0) & 0xff == 27: 
    cv.destroyAllWindows()