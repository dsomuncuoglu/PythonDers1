import cv2
import numpy as np

image=np.zeros((300,300,3),dtype="uint8")

cv2.line(image,(0,0),(100,100),(0,0,255),3)
cv2.imshow("Cizgi",image)

cv2.circle(image,(150,150),25,(0,255,0),3)
cv2.imshow("Cizgi+Daire",image)

cv2.putText(image,"Merhaba",(100,250),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),1)
cv2.imshow("Cizgi+Daire+Metin",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

