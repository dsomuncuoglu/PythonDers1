import cv2
import numpy as np

image=cv2.imread("emma-stone.jpg")

ikiKatBuyuk=cv2.pyrUp(image)

ikiKatKucuk=cv2.pyrDown(image)

print("Orjinal",image.shape)
print("Iki kat buyuk resim",ikiKatBuyuk.shape)
print("Iki kat kucuk resim",ikiKatKucuk.shape)

cv2.imshow("Emma orjinal",image)
cv2.imshow("Iki kat buyuk",ikiKatBuyuk)
cv2.imshow("Iki kat kucuk",ikiKatKucuk)


cv2.waitKey(0)
cv2.destroyAllWindows()