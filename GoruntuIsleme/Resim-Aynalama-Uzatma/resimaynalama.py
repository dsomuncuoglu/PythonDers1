# Resim aynalama, uzatma, tekrar etme, çerçeve oluşturma
import cv2
import numpy as pd


resim=cv2.imread("kemalsunal.jpg")
aynalama=cv2.copyMakeBorder(resim,100,100,200,200,cv2.BORDER_REFLECT) # Aynalama islemi ve boyutları belirtildi.
uzatma=cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_REPLICATE)
tekrarlanan=cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_WRAP)
cerceve=cv2.copyMakeBorder(resim,10,10,10,10,cv2.BORDER_CONSTANT,value=(0,25,255))

cv2.imshow("Kemal Sunal",resim)
cv2.imshow("Aynalanan Resim",aynalama)
cv2.imshow("Uzatilmis olan Resim",uzatma)
cv2.imshow("Tekrarlanan Resim",tekrarlanan)
cv2.imshow("Cerceveli Resim",cerceve)

cv2.waitKey(0)
cv2.destroyAllWindows()
