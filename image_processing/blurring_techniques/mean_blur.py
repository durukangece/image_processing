# in blurring, we simple reduce the edge content and makes the transition form one color to the other very smooth.

# Mean(Average) Blur (Ortalama Bulanıklık):
# Ortalama bulanıklık, bir pikselin çevresindeki bir bölge (kerneller veya filtreler kullanarak) üzerindeki piksellerin ortalamasını alarak bulanıklaştırma işlemidir.
# Bu yöntem görüntüdeki yüksek frekansta detayların kaybolmasına ve görüntüyü daha yumuşak hale getirmesine neden olur.

# Median Blur (Medyan Bulanıklık):
# Medyan bulanıklık, bir pikselin çevresindeki bir bölge üzerindeki piksellerin medyanını alarak bulanıklaştırma işlemidir.
# Medyan, pikselleri sıralandığında ortadaki değeri ifade eder. Bu, aykırı değerlerin etkisini azaltmaya yardımcı olur ve gürültüye karşı daha dirençlidir.
# Medyan bulanıklık, tuz-biber gürültüsü gibi aşırı değerlere sahip pikselleri temizlemek veya görüntüdeki detayları daha iyi korumak için kullanılabilir.

# Gaussian Blur (Gauss Bulanıklık):
# Gauss bulanıklık, bir pikselin çevresindeki bir bölge üzerindeki pikselleri Gauss dağılımına dayalı bir ağırlıklandırma kullanarak bulanıklaştırma işlemidir.
# Bu yöntem, merkeze daha fazla ağırlık veren ve uzak piksellere az ağırlık veren bir Gaussian çekirdek (kernel) kullanır.
# Gauss bulanıklık, genellikle daha doğal ve yumuşak bir bulanıklık efekti yaratmak için kullanılır. Görüntüyü yumuşatırken, kenarlar ve detaylar daha iyi korunabilir.


# import required libraries
import cv2 

# Read the original image
# The input (original image) is 
# loaded and read with opencv imread command   
image = cv2.imread('nisan.png') 
  
# we get output to make sure the image is read
cv2.imshow('original', image) 
cv2.waitKey(0) 

# Average Blur
average = cv2.blur(image,(10,10))
cv2.imshow('Average Blurring', average) 
cv2.waitKey(0) 

# Median Blur 
median = cv2.medianBlur(image, 5) 
cv2.imshow('Median Blurring', median) 
cv2.waitKey(0) 
  
# Gaussian Blur 
gaussian = cv2.GaussianBlur(image, (7, 7), 0) 
cv2.imshow('Gaussian Blurring', gaussian) 
cv2.waitKey(0) 

cv2.destroyAllWindows() 



