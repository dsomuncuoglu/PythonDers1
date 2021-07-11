import cv2
import numpy as np

image=cv2.imread("saturn.jpg",0)

#image=cv2.medianBlur(image,3)

#simple thresholding
ret,thresh1=cv2.threshold(image,100,255,cv2.THRESH_BINARY)

#adaptive thresholding
thresh2=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
thresh3=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

cv2.imshow("Orjinal Resim",image)
cv2.imshow("Simple Thresholding",thresh1)
cv2.imshow("Adaptive Thresholding-Mean",thresh2)
cv2.imshow("Adaptive Thresholding-Gauss",thresh3)

cv2.waitKey(0)
cv2.destroyAllWindows()