import cv2
import numpy as np

image=cv2.imread("parmakizi.jpg",0)
# Simple Treshold
ret,thresh1=cv2.threshold(image,127,255,cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3=cv2.threshold(image,127,255,cv2.THRESH_TRUNC)
ret,thresh4=cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
ret,thresh5=cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)


cv2.imshow("Orjinal Resim",image)
cv2.imshow("Thresh_Binary",thresh1)
cv2.imshow("Thresh_Binary_Inv",thresh2)
cv2.imshow("Thresh_Trunc",thresh3)
cv2.imshow("Thresh_Tozero",thresh4)
cv2.imshow("Thresh_Tozero_Inv",thresh5)

cv2.waitKey(0)
cv2.destroyAllWindows()