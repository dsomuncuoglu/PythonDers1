import cv2
import numpy as np

tablo=cv2.imread("tablo.jpg")
kesit=tablo[140:473,60:315]

kesit[:,:,0]=25 # kesit efektini değiştirme

tablo[130:463,255:510]=kesit # oluşturulan kesiti tanımlanan yere yapıştırır


cv2.imshow("Tablolar",tablo)



cv2.waitKey(0)
cv2.destroyAllWindows()