import cv2
import numpy as np

hababam=cv2.imread("hababam.jpg")


dikdortgen=cv2.rectangle(hababam,(400,200),(250,25),[0,0,255],3) # Resimdeki dikdörtgene alma


cv2.imshow("Hababam Sinifi",hababam)



cv2.waitKey(0)
cv2.destroyAllWindows()