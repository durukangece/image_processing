# THRESHOLD (EŞİKLEME)
# Görüntü bölütleme amacı için kullanılan en önemli yaklaşımlardan birisidir. Birçok görüntü 
# analizi uygulamasında ön işlem olarak tercih edilir. 
# Threshold (Eşikleme) objelerin arkaplandan ayrılması işlemidir ve en basit bölütleme (segmentation) yöntemidir.
# Nesneleri arka plandan ayırmak için en kolay yol, histogramdan göreceli olarak belirlenen bir T eşik değeri ile görüntüdeki piksel değerlerini karşılaştırmak olacaktır.
# Eşikleme Yöntemleri: 1.Bütünsel Eşikleme Yöntemleri(Global Binarization Methods), 2.Yerel Uyarlamalı Eşikleme Yöntemleri (Locally Adaptive Binarization Methods).
# 1.Bütünsel eşikleme yöntemleri: tüm görüntü için tek bir eşik (threshold) değeri hesaplar. Eşik değerinden daha koyu gri seviyesine sahip olan pikseller 
# baskı (print, siyah) olarak etiketlenir. Aksi takdirde arka plan (background, beyaz) olarak etiketlenir.
# 2.Yerel Uyarlamalı Eşikleme Yöntemleri: bir pikselin komşuluğundaki bilgileri temel alarak her bir piksel için bir eşik değeri hesaplar. Bazı yöntemler tüm görüntü 
# üzerinde bir eşik değeri hesaplar. Eğer giriş görüntüsündeki bir (x, y) pikseli (x, y)’de hesaplanan eşik yüzeyinden daha yüksek gri seviyesine sahipse bu (x, y) pikseli  
# arka plan olarak etiketlenir. Aksi halde baskı olarak etiketlenir.
# Şimdi kullanacağımız yöntem olan Adaptive Threshold, yerel eşikleme yöntemidir. 

# Depending on your project, leveraging adaptive thresholding can enable you to:
# 1.Obtain better segmentation than using global thresholding methods, such as basic thresholding and Otsu thresholding.
# 2.Avoid the time consuming and computationally expensive process of training a dedicated Mask R-CNN or U-Net segmentation network.

# What is adaptive thresholding? And how is adaptive threshold different from “normal” thresholding?
# Basit eşikleme yöntemleri kullanmanın dezavantajlarından biri, eşik değerimizi manuel olarak sağlamamızın gerekmesidir.
# Ayrıca, iyi bir T değeri bulmak birçok manuel deney ve parametre ayarlaması gerektirebilir ve bu da çoğu durumda pratik değildir.
# Bu sorunun üstesinden gelmek için, piksellerin küçük komşularını dikkate alan ve daha sonra her bir komşu için en uygun eşik değeri T'yi bulan 
# uyarlanabilir eşiklemeyi (adaptive thresholding) kullanabiliriz.

# ADAPTIVE THRESHOLDING: Apply adaptive thresholding based on Local features over an image.
# Adaptif eşiklemede, resmin küçük bir bölgesi için eşik değeri hesaplanır. Bu nedenle aynı 
# görüntünün farklı bölgelerinde farklı eşikler elde ediyoruz ve farklı aydınlatmalara sahip 
# görüntüler için daha iyi sonuç vermektedir. 

# Adaptif eşiklemede, eşik değerinin nasıl hesaplanacağına karar veren iki yöntem mevcuttur.
# ADAPTIVE_THRESH_MEAN_C: Eşik değeri komşu piksellerin alanlarının ortalamasıdır. 
# ADAPTIVE_THRESH_GAUSSIAN_C: Eşik değeri, ağırlıkların bir gaussian penceresi olduğu komşuluk 
# değerlerinin ağırlıklı toplamıdır.  


# import required libraries
import cv2  
   
# Read the original image
# The input (original image) is 
# loaded and read with opencv imread command
original_image = cv2.imread('kerem.png')  #original image
   
# convert the image in grayscale  
img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY) 

# we get output to make sure the image is read
cv2.imshow('Original Image', original_image) 
cv2.waitKey(0) 
   
# applying different thresholding  
# techniques on the input image:

# adaptive mean
thresh1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, # 255: eşikleme sonucunda beyaz olarak işaretlenen piksellerin yoğunluğunu ifade eder.
                                          cv2.THRESH_BINARY, 199, 5)  # 199: adaptif eşiklemenin hesaplanmasında kullanılan yerel eşik değerini temsil eder. Yani, bu değer, 
                                                                      # piksellerin çevresindeki belirli bir bölgedeki ortalamayı hesaplarken kullanılan eşik değerini ifade eder.
                                                                      # 5:  Bu değer ise adaptif eşiklemenin etkili olabilmesi için kullanılan bölge boyutunu belirtir. 
                                                                      # Yani, ortalama hesaplamalarının hangi boyutta bir pencere kullanılarak yapılacağını gösterir. 
                                                                      # 5, bu hesaplamaların 5x5 piksellik bir pencere kullanılarak gerçekleştirileceğini ifade eder.
cv2.imshow('Adaptive Mean', thresh1)# the window showing output images  
  
# adaptive gaussian
thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                          cv2.THRESH_BINARY, 199, 5)  
cv2.imshow('Adaptive Gaussian', thresh2) # the window showing output images
       
# De-allocate any associated memory usage   
if cv2.waitKey(0) & 0xff == 27:  # press esc to close the window
    cv2.destroyAllWindows()  