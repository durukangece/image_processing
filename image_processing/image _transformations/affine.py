# import required libraries  
import cv2
import numpy as np

# Read the original image
# The input (original image) is 
# loaded and read with opencv imread command
image = cv2.imread('okcukiz.png')

# we get output to make sure the image is read
cv2.imshow('Original Image', image) 
cv2.waitKey(0) 

# Görüntü boyutlarını al
height, width = image.shape[:2]

# Kaydırma matrisini oluştur
# Örneğin, görüntüyü yatayda 50 piksel sağa kaydıralım
translation_matrix = np.float32([[1, 0, 50], [0, 1, 0]])

# warpAffine işlemini uygula
shifted_image = cv2.warpAffine(image, translation_matrix, (width, height))

# Sonucu göster
cv2.imshow('Shifted Image', shifted_image)
cv2.imwrite('affine.png', shifted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
