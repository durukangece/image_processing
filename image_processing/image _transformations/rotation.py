# import required libraries
import cv2

# Read the original image
# The input (original image) is 
# loaded and read with opencv imread command
img = cv2.imread('okcukiz.png')

# we get output to make sure the image is read
cv2.imshow('Original Image', img) 
cv2.waitKey(0) 

# rotate the image by 180 degree clockwise
img_cw_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# display the rotated image
cv2.imshow("Image rotated by 180 degree", img_cw_90)
cv2.imwrite('rotation.png', img_cw_90)
cv2.waitKey(0)
cv2.destroyAllWindows()