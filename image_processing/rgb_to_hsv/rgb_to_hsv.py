# RGB(Red, Green, Blue) renk uzayı, renkleri kırmızı(R), yeşil(G) ve mavi(B) bileşenlerin karışımı olarak temsil eder. Her piksel için üç bileşen içerir ve her bir bileşen 0 ile 255 arasında değer alır.

# HSV (Hue, Saturation, Value) renk uzayı ise renkleri üç temel özellikle temsil eder:
# 1.Hue(Ton): Renkin temel tonunu temsil eder (örneğin, kırmızı, yeşil, mavi).
# 2.Saturation(Doygunluk): Renklerin canlılığını veya solgunluğunu gösterir.
# 3.Value(Parlaklık): Renkli nesnelerin parlaklığını veya koyuluğunu ifade eder.

# RGB bileşenleri 0 ile 255 arasında değerler alırken, HSV bileşenleri farklı aralıklarda ifade edilir:
# Hue(Ton): Genellikle 0 ile 360 derece arasında bir değerle ifade edilir.
# Saturation(Doygunluk) ve Value(Parlaklık): Genellikle 0 ile 100 arasında yüzde birimiyle ifade edilir.

# Neden dönüşüm yaparız?: 
# HSV renk uzayı, renklerin tonunu, doygunluğunu ve parlaklığını ayrı ayrı ele almanıza olanak tanır. 
# Bu, renk tabanlı nesne tespiti, parlaklık düzeltilmesi ve renk filtreleme gibi uygulamalarda faydalıdır.



# import required libraries
import cv2

# Read the original image
# The input (original image) is 
# loaded and read with opencv imread command 
bgr_img = cv2.imread('Childhood.png') 

# yüklenen görsel, varsayılan olarak RGB renk uzayındadır. 

# we get output to make sure the image is read
cv2.imshow('Original Image', bgr_img) 
cv2.waitKey(0) 

# Convert the BGR image to HSV Image
hsv_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2HSV)
cv2.imwrite('hsv_image.png', hsv_img)

# Display the HSV image
cv2.imshow('HSV image', hsv_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
