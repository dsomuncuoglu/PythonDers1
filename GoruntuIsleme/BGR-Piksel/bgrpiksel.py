import cv2 # OpenCV kutuphanesinin cagrilmasi
import numpy as np # Numpy kutuphanesinin cagrilmasi

aslan=cv2.imread("aslan.jpg")

aslan2=aslan.copy() # resmi değişkene kopyalama
aslan3=aslan.copy()
aslan4=aslan.copy()

aslan2[15,15]=[0,0,255] # girilen noktanın rengini değiştirme
aslan2[50,:]=[0,0,255] # girilen değerlerin rengini değiştirme

aslan3[:,:,0]=15 # 0=mavi , 1=yesil , 2=kırmızı renk efekt
aslan3[:,:,1]=222

aslan4[125:150,315:400,0]=0 # Belirlenen bir alanı efekt ekleme
aslan4[125:150,315:400,1]=0 # y[],x[] kısımlarına göre yapılır.
aslan4[125:150,315:400,2]=0 

cv2.imshow("Orjinal Aslan Resmi",aslan)
cv2.imshow("BGR degistirilmis aslan resmi",aslan2)
cv2.imshow("Efektli aslan resmi",aslan3)
cv2.imshow("Belirli bir alan efektli aslan resmi",aslan4)

print(aslan2[(0,0)]) # Resimin [0,0] daki BGR değeri
print("Resim boyutu:",aslan.size)
print("Resmin özellikleri:",aslan.shape)
print("Resmin veri tipi:",aslan.dtype)


cv2.waitKey(0)
cv2.destroyAllWindows()