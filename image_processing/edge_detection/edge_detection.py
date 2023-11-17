# Canny Edge Detector:
# Canny kenar tespiti, çok adımlı bir süreç kullanarak yüksek hassasiyetli kenarları tespit eden yaygın bir yöntemdir. 
# Gürültüyü azaltma, türev hesaplama, kenar gücü hesaplama ve kenar tespiti aşamalarından oluşur

# Sobel operatörü, görüntü işleme alanında kullanılan bir kenar tespiti (edge detection) yöntemi ve görüntü iyileştirme tekniğidir. Sobel 
# operatörü, bir görüntü üzerindeki yoğunluk değişikliklerini ve kenarları vurgulamak için kullanılır. 
# Bu operatör, görüntüdeki piksellerin türevlerini hesaplar ve bu türevlerin büyüklüğünü kenarları gösteren bir kenar haritası olarak sunar.
# Sobel X filtresi: Bu filtre, görüntünün yatay yoğunluk değişikliklerini yakalamak için kullanılır. 
# Sobel Y filtresi: Bu filtre, görüntünün dikey yoğunluk değişikliklerini yakalamak için kullanılır. Dikey kenarları tespit etmek için etkilidir.

# Sobel operatörü, görüntü işleme uygulamalarında kenar tespiti, kenar iyileştirme, nesne tespiti ve nesne takibi gibi birçok görevde kullanılır. 
# Sobel operatörü, basit bir yöntem olmasına rağmen, görüntüdeki önemli bilgileri ortaya çıkarmak için çok etkilidir ve daha karmaşık kenar tespiti algoritmalarının temelini oluşturur.

# Canny vs Sobel 
# Sobel:
# İşlemi basittir: Basit İşlem: Sobel, görüntünün gradyanını (renk değişikliği) hesaplamak için basit bir fark işlemi kullanır. 
# Bu, kenarları tespit etmek için yeterli olabilir, ancak bazı durumlarda gürültülü sonuçlara neden olabilir.
# Kenar Kalınlığı: Sobel, tespit edilen kenarların kalınlığını belirtmez. Sadece kenarların konumunu belirler.
# Daha Hızlı İşlem: Sobel, Canny'ye göre daha hızlı bir işlem yapar ve daha basit bir algoritmaya sahiptir.

# Canny:
# Çok Aşamalı İşlem: Canny, çok aşamalı bir işlem kullanır. Gürültüyü azaltma, kenarları algılama ve kenarları iyileştirme aşamalarından oluşur. Bu, daha hassas ve daha iyi sonuçlar üretir.
# Kenar Kalınlığı: Canny, kenarların kalınlığını da hesaplar. Bu, kenarların daha geniş bir bölgede tanımlanmasına olanak tanır.
# Daha Karmaşık İşlem: Canny, Sobel'e göre daha karmaşık bir algoritma kullanır ve daha fazla hesaplama gerektirir.


# import required libraries
import cv2
 
# Read the original image
# The input (original image) is 
# loaded and read with opencv imread command
img = cv2.imread('erkm_abim.png') 

# we get output to make sure the image is read
cv2.imshow('Original Image', img) 
cv2.waitKey(0) 
 
# Convert to graycsale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 
 
# Sobel Edge Detection
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
# Display Sobel Edge Detection Images
cv2.imshow('Sobel X', sobelx)
cv2.imwrite('sobelx.png', sobelx)
cv2.waitKey(0)

cv2.imshow('Sobel Y', sobely)
cv2.imwrite('sobely.png', sobely)
cv2.waitKey(0)

cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
cv2.imwrite('sobelxy.png', sobelxy)
cv2.waitKey(0)
 
# Canny Edge Detection
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
# Display Canny Edge Detection Image
cv2.imshow('Canny Edge Detection', edges)
cv2.imwrite('canny.png', edges)
cv2.waitKey(0)
 
cv2.destroyAllWindows()

# Sobel ve Canny kenar algılayıcıları, farklı uygulamalarda kullanılmak üzere tasarlanmıştır. Sobel, basit ve hızlı bir kenar tespit yöntemidir ve bazı durumlarda yeterli olabilir. 
# Canny ise daha sofistike ve hassas bir yöntemdir ve genellikle daha doğru sonuçlar sağlar. Seçiminiz, projenizin gereksinimlerine ve performans hedeflerine bağlı olacaktır.