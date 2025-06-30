### Bitwise Operations on image

import cv2 as cv
import numpy as np

image1 = cv.imread('image\img3.png')    
image2 = cv.imread('image\img4.png')

# bitwiseAnd = cv.bitwise_and(image1, image2, mask=None)  ## Bitwise AND
# bitwiseOr = cv.bitwise_or(image1, image2, mask=None)  ## Bitwise OR 
# bitwiseXor = cv.bitwise_xor(image1, image2, mask=None)  ## Bitwise XOR
bitwiseNot1 = cv.bitwise_not(image1, mask=None)  ## Bitwise NOT 
bitwiseNot2 = cv.bitwise_not(image2, mask=None)  ## Bitwise NOT


cv.imshow("Bitwise NOT 1", bitwiseNot1)    ## To show the image on display
cv.imshow("Bitwise NOT 2", bitwiseNot2)    ## To show the image on display


if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()


### In this code the img3 and img4 is not of same size so the program throws an error(Array size not same)




