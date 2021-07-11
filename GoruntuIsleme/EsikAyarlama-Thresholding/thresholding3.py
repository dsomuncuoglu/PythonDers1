import cv2
import numpy as np

image=cv2.imread("saturn.jpg",0)

#simple thresholding
ret,thresh1=cv2.threshold(image,127,255,cv2.THRESH_BINARY)

#otsu thresholding
ret,thresh2=cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("Orjinal Resim",image)
cv2.imshow("Simple Thresholding",thresh1)
cv2.imshow("Otsu Thresholiding",thresh2)

cv2.waitKey(0)
cv2.destroyAllWindows()