# Erozyon (Erosion):
# Erozyon işlemi, nesnelerin kenarlarını aşındırarak küçültmeyi amaçlar.
# Bir kernel (genellikle 3x3 veya 5x5 boyutunda) kullanılır ve bu kernel görüntünün her pikseli üzerine yerleştirilir.
# Eğer kernelin içindeki tüm pikseller siyah (0) ise, o pikselin değeri erozyon işlemi sonucu siyah olarak kalır. Aksi durumda, o piksel beyaz (1) yapılır.
# Erozyon işlemi küçük gürültülerin giderilmesi ve nesne kenarlarının vurgulanması için kullanışlıdır.

# Genişleme (Dilation):
# Genişleme işlemi, nesneleri büyütmeyi amaçlar.
# Yine bir kernel kullanılır ve kernel görüntünün her pikseli üzerine yerleştirilir.
# Eğer kernel içinde en az bir piksel beyaz (1) ise, merkez piksel beyaz yapılır. Bu işlem nesnelerin büyümesini sağlar.

# Açma (Opening):
# Açma işlemi, erozyon ve genişleme işlemlerinin birleşiminden oluşur. İlk olarak erozyon işlemi uygulanır, ardından genişleme işlemi uygulanır.
# Açma işlemi, küçük gürültülerin giderilmesi ve nesnelerin şeklinin korunmasına yardımcı olur.

# Kapatma (Closing):
# Kapatma işlemi, genişleme ve erozyon işlemlerinin birleşiminden oluşur. İlk olarak genişleme işlemi uygulanır, ardından erozyon işlemi uygulanır.
# Kapatma işlemi, nesnelerin deliklerinin kapatılmasına ve nesnelerin birleştirilmesine yardımcı olur.

# import required libraries
import cv2 
import numpy as np

# The input (original image) is 
# loaded and read with opencv imread command, 
#'cv.IMREAD_GRAYSCALE)' function reads the 
# loaded image by converting it to grayscale.
img = cv2.imread('library.png', cv2.IMREAD_GRAYSCALE)

# we get output to make sure the image is read
cv2.imshow('Original Image', img) 
cv2.waitKey(0) 

assert img is not None, "file could not be read, check with os.path.exists()"
kernel = np.ones((5,5),np.uint8)

erosion = cv2.erode(img,kernel,iterations = 1)
dilation = cv2.dilate(img,kernel,iterations = 1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imshow('Erosion', erosion)
cv2.imwrite('erosion.png', erosion)
cv2.waitKey(0)

cv2.imshow('Dilation', dilation)
cv2.imwrite('dilation.png', dilation)
cv2.waitKey(0)

cv2.imshow('Opening', opening)
cv2.imwrite('opening.png', opening)
cv2.waitKey(0)

cv2.imshow('Closing', closing)
cv2.imwrite('closing.png', closing)
cv2.waitKey(0)

cv2.destroyAllWindows()
