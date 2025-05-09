import cv2 as cv

img = cv.imread('image/isro.jpeg')

cv.imshow('Isro', img)

cv.wailKey(0)
