import cv2
import numpy as np

camera=cv2.VideoCapture(0)

while True:
    ret,goruntu=camera.read()

    cv2.rectangle(goruntu,(100,100),(200,200),(0,0,255),2)
    cv2.line(goruntu,(0,0),(100,100),(255,0,0),2)
    cv2.circle(goruntu,(200,200),25,(0,255,0),2)
    cv2.putText(goruntu,"Merhaba",(250,250),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)

    cv2.imshow("Kamera",goruntu)
    if cv2.waitKey(24)==ord('q'):
        break

camera.release()
cv2.destroyAllWindows()