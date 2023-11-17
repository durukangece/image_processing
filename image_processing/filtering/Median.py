# import required libraries
import cv2
import numpy as np

# Read the original image
# The input (original image) is 
# loaded and read with opencv imread command
img = cv2.imread('gizem.png')

# we get output to make sure the image is read
cv2.imshow('Original Image', img) 
cv2.waitKey(0) 

median = cv2.medianBlur(img, 5)
compare = np.concatenate((img, median), axis=1) #side by side comparison

cv2.imshow('img', compare)
cv2.imwrite('median.png', median)
cv2.waitKey(0)
cv2.destroyAllWindows