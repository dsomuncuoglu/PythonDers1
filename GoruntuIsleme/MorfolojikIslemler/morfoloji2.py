import cv2
import numpy as np


image=cv2.imread("b.jpg")

kernel=np.ones((5,5),np.uint8)

opening=cv2.morphologyEx(image,cv2.MORPH_OPEN,kernel)
closing=cv2.morphologyEx(image,cv2.MORPH_CLOSE,kernel)
gradyan=cv2.morphologyEx(image,cv2.MORPH_GRADIENT,kernel)
tophat=cv2.morphologyEx(image,cv2.MORPH_TOPHAT,kernel)
blackhat=cv2.morphologyEx(image,cv2.MORPH_BLACKHAT,kernel)

cv2.imshow("Orjinal Resim",image)
cv2.imshow("Morph_open",opening)
cv2.imshow("Morph_close",closing)
cv2.imshow("Morph_gradient",gradyan) # dilation-erosion=gradient
cv2.imshow("Morph_tophat",tophat) # orjinal-opening=tophat
cv2.imshow("Morph_blackhat",blackhat) # orjinal-closing=blackhat

cv2.waitKey(0)
cv2.destroyAllWindows()