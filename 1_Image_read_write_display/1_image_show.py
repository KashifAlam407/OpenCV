 
import cv2 as cv

# print("cv.__version__")   ### For printing version of openCV (cv2)

#### cv.imread(path, value[1,0,-1]) --- it is used to read the image using path of the image
# img = cv.imread('image/nature.webp', cv.IMREAD_COLOR)   ### OR below line 
# img = cv.imread('image/nature.webp', 1)

# img = cv.imread('image/nature.webp', cv.IMREAD_GRAYSCALE)  ### OR bleow line
# img = cv.imread('image/nature.webp', 0)


# img = cv.imread('image/nature.webp', cv.IMREAD_UNCHANGED)   ### OR bleow line 
img = cv.imread('image/nature.webp', -1)    


# img = cv.imread('image/nature_large.webp')

cv.imshow('Isro', img)

print(img.shape)   ### Used to show the height, width and channel of image using shape attribute

cv.waitKey(0)
    