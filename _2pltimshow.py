import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

path = 'image/nature.webp'

img = cv.imread(path)

plt.imshow(img)

plt.waitforbuttonpress()

plt.close('all')

