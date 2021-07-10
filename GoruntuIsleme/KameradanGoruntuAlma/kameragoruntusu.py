import cv2
import numpy as np


camera=cv2.VideoCapture(0)  # 0-Bilgisayar Kamerasını alır, 
#camera2=cv2.VideoCapture(1) # 1-USB'ye bağlı olan kamerayı alır
                            # 2- Bilgisayar üzerinde hazır olan videoların seçimi

while True:
    ret,goruntu=camera.read()
    #ret,goruntu2=camera2.read()
    cv2.imshow("Kamera Goruntusu",goruntu)
    #cv2.imshow("Kamera Goruntusu2",goruntu2)
    if cv2.waitKey(30)==ord('q'):
        break


camera.release()
cv2.destroyAllWindows()