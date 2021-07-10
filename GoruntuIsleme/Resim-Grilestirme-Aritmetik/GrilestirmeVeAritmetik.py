import cv2
import numpy as np

mehmet=cv2.imread("mehmetalierbil.png")
cv2.imshow("Mehmet Ali Erbil",mehmet)

yukseklik,genislik,kanalSayisi=mehmet.shape
print("Orjinal resmin","Yükseklik=",yukseklik,"Genişlik=",genislik,"Kanal Sayisi=",kanalSayisi)

mehmetGri=cv2.cvtColor(mehmet,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gri resim",mehmetGri)

mehmetGri2=cv2.imread("mehmetalierbil.png",0)
cv2.imshow("Gri resim2",mehmetGri2)

yukseklik_gri,genislik_gri=mehmetGri.shape # Resim gri olduğu için kanal sayisi 1'dir.
print("Gri resmin","Yükseklik=",yukseklik_gri,"Genişlik=",genislik_gri)

cv2.waitKey(0)
cv2.destroyAllWindows()