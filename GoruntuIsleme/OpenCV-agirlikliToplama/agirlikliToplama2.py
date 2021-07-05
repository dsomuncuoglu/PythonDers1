import cv2
import numpy as pd

ibrahim=cv2.imread("ibrahimtatlises.jpg")
mahmut=cv2.imread("mahmuttuncer.jpg")

cv2.imshow("Ibrahim Tatlises",ibrahim)
cv2.imshow("Mahmut Tuncer",mahmut)

'''Toplam yaparken resimlerin boyutu aynı olmak zorundadır.'''

toplam=cv2.add(ibrahim,mahmut) # resimleri eşit bir şekilde üst üste getirir.
cv2.imshow("Toplam olan resim",toplam) 

agirliklitoplam=cv2.addWeighted(ibrahim,0.7,mahmut,0.3,0) # resimleri ağırlığına bağlı olarak getirir.
cv2.imshow("Agirlikli toplam olan resim",agirliklitoplam)


cv2.waitKey(0)
cv2.destroyAllWindows()