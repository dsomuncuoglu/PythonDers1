import cv2
import numpy as pd

ibrahim=cv2.imread("ibrahimtatlises.jpg")
mahmut=cv2.imread("mahmuttuncer.jpg")




print(ibrahim[255,400])
print(mahmut[400,400])

print(ibrahim[255,400]+mahmut[400,400])


ibrahim[200:250,0:50]=ibrahim[255,400]+mahmut[400,400]

cv2.imshow("Ibrahim Tatlises",ibrahim)
cv2.imshow("Mahmut Tuncer",mahmut)


cv2.waitKey(0)
cv2.destroyAllWindows()