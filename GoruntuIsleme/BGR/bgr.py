import cv2 # OpenCV kutuphanesinin cagrilmasi
import numpy as np # Numpy kutuphanesinin cagrilmasi

resim=cv2.imread("kus.jpg") # Kuş resminin okunması

resim2=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY) # Kuş resminin gri renge çevirilmesi

cv2.imshow("Kuslar Renkli",resim) # Kuş resminin kullanıcıya gösterilmesi

cv2.imshow("Kuslar Gri",resim2)

print(resim) # Resimdeki renkler her pikselin matrisel yapısıdır. Bütün matrisler toplanıp resim oluşur.

print("Renkli Resim Bilgileri\n-------------------------")
print(resim.size) # Resim boyutunu gösterir.
print(resim.dtype) # Resim veri tipini verir.
print(resim.shape) # Resimin genişlik,yüksekliği ve 3 kanallı(BGR) olduğu belirtilir.(Çıkan 3 sayının çarpımı bize resim boyutunu verir)

print("Gri Resim Bilgileri\n-------------------------")
print(resim2.size) # Resim boyutunu gösterir.
print(resim2.dtype) # Resim veri tipini verir.
print(resim2.shape) # Resimin genişlik,yüksekliği ve 1 kanallı(BGR) olduğu belirtilir. Resim gri olduğu için tek kanallıdır.

cv2.waitKey(0)
cv2.destroyAllWindows()


