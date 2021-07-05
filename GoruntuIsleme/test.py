import numpy as np
import cv2

foto=cv2.imread('peakup.jpg')

fotoGri=cv2.cvtColor(foto,cv2.COLOR_BGR2GRAY)

ret,fotoBW=cv2.threshold(fotoGri,110,240,cv2.THRESH_BINARY)

cv2.imwrite("peakupGri.jpg",fotoGri)

cv2.imshow('Binary Foto',fotoBW)

cv2.imshow('Orijinal Foto',foto)

cv2.imshow('Gri tona sahip foto',fotoGri)

cv2.imwrite("peakupBW.jpg",fotoBW)

cv2.waitKey(0)

cv2.destroyAllWindows()