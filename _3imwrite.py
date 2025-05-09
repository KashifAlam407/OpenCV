import cv2 as cv
import os

image_path = r'F:\OpenCV\image\isro2.jpeg'  ## here r is used to treat \ as a literial not an escape character.

directory = r'F:\OpenCV\image'

## reading the image
img = cv.imread(image_path)

os.chdir(directory)

print("Before saving image: ")
print(os.listdir(directory))

## filename 
filename = 'savedImage.jpeg'

## saving the image
cv.imwrite(filename, img)

print("After saving the image")
print(os.listdir(directory))
print('Successfully saved')
