### Visualizing the different color channels of an RGB image

import cv2 as cv

image = cv.imread('F:\OpenCV\image\isro2.jpeg')

B, G, R = cv.split(image)


### gives the data of image in matrix form
# print(B)
# print("")
# print(G)
# print("")
# print(R)
# print("")
# print(image)   


cv.imshow("Original", image)
cv.waitKey(0)

cv.imshow("Blue", B)
cv.waitKey(0)

cv.imshow("Green", G)
cv.waitKey(0)

cv.imshow("Red", R)  
cv.waitKey(0)


cv.destroyAllWindows() 