import cv2
from matplotlib import pyplot as plt

# Renkli olarak görüntüyü okuyun
img = cv2.imread('gizem.png')

# Renkli görüntüyü gösterin
plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original')
plt.xticks([]), plt.yticks([])

# Görüntüyü bulanıklaştırın
blur = cv2.blur(img, (5, 5))

# Bulanıklaştırılmış görüntüyü gösterin
plt.subplot(122), plt.imshow(cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)), plt.title('Blurred')
plt.xticks([]), plt.yticks([])

cv2.imwrite('aveage.png', blur)

plt.show()

