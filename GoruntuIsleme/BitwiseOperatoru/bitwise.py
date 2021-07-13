import cv2
import numpy as np


image1=cv2.imread("a.png")
image2=cv2.imread("b.png")

bit_And=cv2.bitwise_and(image1,image2)
bit_Or=cv2.bitwise_or(image1,image2)
bit_XOR=cv2.bitwise_xor(image1,image2)
bit_Not1=cv2.bitwise_not(image1)
bit_Not2=cv2.bitwise_not(image2)

cv2.imshow("Birinci Resim",image1)
cv2.imshow("Ikinci Resim",image2)
cv2.imshow("bitwise and",bit_And)
cv2.imshow("bitwise or",bit_Or)
cv2.imshow("bitwise xor",bit_XOR)
cv2.imshow("bitwise not1",bit_Not1)
cv2.imshow("bitwise not2",bit_Not2)

cv2.waitKey(0)
cv2.destroyAllWindows()