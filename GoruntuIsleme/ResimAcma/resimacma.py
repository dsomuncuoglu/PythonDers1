import cv2 # Opencv kütüphanesinin çağrılması
import numpy as np # Numpy kütüphanesinin çağrılması

resim=cv2.imread("logo.png",0) # 0 yapılırsa BGR renkler kullanılmaz.

cv2.imshow("Logo Goruntusu",resim) # Logonun cv2 ile görüntülenmesi

cv2.imwrite("yenilogo.png",resim) # Logonun değiştirilmiş halinin dosyaya kaydedilmesi


cv2.waitKey(0) # Herhangi bir tuşa basılana kadar Logonun ekranda kalmasının sağlanması
cv2.destroyAllWindows() # cv2 ile yapılan tüm işlemlerin windowsta kapatılması

