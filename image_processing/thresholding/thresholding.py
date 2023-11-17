# Basit eşikleme (thresholding), bir renkli veya gri tonlamalı görüntüyü siyah ve beyaz bir görüntüye dönüştürme işlemidir. 
# Bu işlem, bir eşik değeri (threshold value) belirleyerek gerçekleştirilir. Her piksel, eşik değerine göre karşılaştırılır 
# ve bu karşılaştırmaya dayalı olarak piksel ya beyaz (255) veya siyah (0) olarak ayarlanır.

#Eşikleme Yöntemleri 

# THRESH_BINARY:
# Kullanım Senaryosu: Görüntüdeki bir nesnenin veya bölgenin belirli bir parlaklık aralığını (örneğin, parlak veya karanlık bölgeler) ayırmak istendiğinde kullanılır.
# Örnek: Karanlık nesneleri beyaz bir arka plan üzerinde belirlemek.

# THRESH_BINARY_INV:
# Kullanım Senaryosu: Görüntüdeki bir nesnenin veya bölgenin belirli bir parlaklık aralığını dışındakileri ayırmak istendiğinde kullanılır.
# Örnek: Parlak nesneleri siyah bir arka plan üzerinde belirlemek.

# THRESH_TRUNC:
# Kullanım Senaryosu: Görüntüde belirli bir parlaklık eşik değerini aşan değerlerin kesilmesini istediğinizde kullanılır.
# Örnek: Belirli bir parlaklığı aşan değerleri diğer değerlerle kesmek.
# Eşik değerini aşan piksellerin değerleri korunur (yani değişmez).
# Eşik değerini aşmayan piksellerin değerleri ise eşik değeri ile aynı değere (eşik değeri) ayarlanır.
# Bu, görüntünün parlaklık değerlerini sınırlar. Eşik değeri olarak seçilen değer, parlaklık değerlerini sınırlamak veya düzenlemek istediğiniz değere göre belirlenir.
# Bu yöntem, bazı durumlarda görüntüdeki belirli parlaklık değerlerini sınırlamak veya düzenlemek istendiğinde kullanışlı olabilir. Özellikle görüntünün parlaklık aralığını daraltmak veya belirli parlaklık değerlerini yeniden düzenlemek için kullanılabilir.

# THRESH_TOZERO:
# Kullanım Senaryosu: Görüntüde belirli bir parlaklık eşik değerini aşan değerleri korumak istediğinizde kullanılır.
# Örnek: Belirli bir parlaklığı aşan değerleri korumak ve diğerlerini sıfıra düşürmek.
#  ikili eşikleme yöntemlerinden biridir ve görüntü işleme uygulamalarında sıkça kullanılır. Bu yöntem, bir gri tonlamalı görüntüyü iki farklı şekilde işler:
# Eşik değerini aşan piksellerin değerleri korunur (yani değişmez).
# Eşik değerini aşmayan piksellerin değerleri sıfıra (siyah) ayarlanır.
# Bu, özellikle belirli bir parlaklık eşik değerini aşan piksellerin değerlerini korumak istediğiniz durumlarda kullanışlıdır. 
# Bu yöntemi kullanarak, belirli bir parlaklık değerinin altındaki pikselleri siyah yapabilir ve eşik değerini aşan pikselleri orijinal değerlerini koruyabilirsiniz.
# Bu yöntem, görüntü üzerinde nesneleri veya bölgeleri belirlemek veya belirli bir parlaklık eşiği altındaki detayları göz ardı etmek istendiğinde kullanışlıdır. 
# Özellikle nesneleri ayırmak veya belirli parlaklık değerlerini işlemek için kullanılır.

# THRESH_TOZERO_INV:
# Kullanım Senaryosu: Görüntüde belirli bir parlaklık eşik değerini aşan değerleri sıfıra düşürmek istediğinizde kullanılır.
# Örnek: Belirli bir parlaklığı aşan değerleri sıfıra düşürmek ve diğerlerini korumak.
# Yani, bu yöntem eşik değerini aşan bölgeleri siyahlaştırırken, eşik değerini aşmayan bölgeleri orijinal değerlerini korur.
# görüntü üzerinde belirli bir parlaklık eşiği aşan bölgeleri işlemek istediğiniz durumlar için kullanışlıdır. 
# Özellikle eşik değeri üzerindeki parlaklık değerlerini azaltmak veya belirli parlaklık eşiklerinin altındaki detayları vurgulamak için kullanılır.

# import required libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt

# The input (original image) is 
# loaded and read with opencv imread command, 
#'cv.IMREAD_GRAYSCALE)' function reads the 
# loaded image by converting it to grayscale.
img = cv2.imread('zipzip.png', cv2.IMREAD_GRAYSCALE)

# we get output to make sure the image is read
cv2.imshow('Original Image', img) 
cv2.waitKey(0) 

assert img is not None, "file could not be read, check with os.path.exists()"
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
 plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
 plt.title(titles[i])
 plt.xticks([]),plt.yticks([])
plt.show()