# renk histogramının temel kavramlarına bir göz atalım:

# 1.Renk Uzayları (Color Spaces): 
# Bir görüntüdeki renkler, bir renk uzayında temsil edilir. 
# En yaygın olarak kullanılan renk uzayları RGB (Red, Green, Blue), HSV (Hue, Saturation, Value), LAB (Lightness, A, B) ve YUV'dur. Her renk uzayı, renkleri farklı şekillerde temsil eder.

# 2.Histogramın Hesaplanması: 
# Renk histogramı, bir görüntü üzerinde belirli bir renk uzayında piksellerin dağılımını gösteren bir grafiktir. Histogram hesaplaması, 
# her pikselin renk değerlerini renk aralıklarına (örneğin, 0-255) göre sayarak yapılır. Bu, her renk aralığındaki piksel sayısını temsil eden histogram değerlerini üretir.

# 3.Görselleştirme: 
# Histogram değerleri, bir çubuk grafik olarak görselleştirilir. Genellikle çubuk grafikler, 
# renklerin yoğunluğunu yatay eksende temsil ederken, piksel sayısını dikey eksende gösterir.

# Python'da renk histogramını yazdırmak ve görselleştirmek için tipik olarak şu adımlar takip edilir:

# 1.Görüntü renk uzayına dönüştürülür (genellikle RGB'den başka bir renk uzayına).
# 2.Her renk kanalının histogramı hesaplanır (örneğin, kırmızı, yeşil, mavi).
# 3.Histogramlar Matplotlib veya benzeri bir grafik kütüphanesi kullanılarak çizilir.

# bu kodda varsayılan(RGB) format üzerinden histogram oluşturacağız. 

# import required libraries
import cv2
import matplotlib.pyplot as plt

# Read the original image
# The input (original image) is 
# loaded and read with opencv imread command
img = cv2.imread('gizem.png')

# we get output to make sure the image is read
cv2.imshow('Image', img)
cv2.waitKey(0)

# convert the image in grayscale  
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 

red_hist = cv2.calcHist([img], [0], None, [256], [0, 255])
green_hist = cv2.calcHist([img], [1], None, [256], [0, 255])
blue_hist = cv2.calcHist([img], [2], None, [256], [0, 255])

plt.subplot(4, 1, 1)
plt.imshow(img)
plt.title('image')
plt.xticks([])
plt.yticks([])

plt.subplot(4, 1, 2)
plt.plot(red_hist, color='r')
plt.xlim([0, 255])
plt.title('red histogram')

plt.subplot(4, 1, 3)
plt.plot(green_hist, color='g')
plt.xlim([0, 255])
plt.title('green histogram')

plt.subplot(4, 1, 4)
plt.plot(blue_hist, color='b')
plt.xlim([0, 255])
plt.title('blue histogram')

plt.tight_layout()
plt.show()