import cv2


image=cv2.imread("a.png")
meanFilter=cv2.blur(image,(3,3)) # Doğrusal filtreleme
meanFilter2=cv2.blur(image,(5,5))

medianFilter=cv2.medianBlur(image,3) # Doğrusal olmayan filtreleme
medianFilter2=cv2.medianBlur(image,5)

gaussFilter=cv2.GaussianBlur(image,(3,3),0)
gaussFilter2=cv2.GaussianBlur(image,(5,5),0)

cv2.imshow("Orjinal Resim",image)
cv2.imshow("Mean Filter(3x3)",meanFilter)
cv2.imshow("Mean Filter(5x5)",meanFilter2)
cv2.imshow("Median Filter(3x3)",medianFilter)
cv2.imshow("Median Filter(5x5)",medianFilter2)
cv2.imshow("Gauss Filter(3x3)",gaussFilter)
cv2.imshow("Gauss Filter(5x5)",gaussFilter2)

cv2.waitKey(0)
cv2.destroyAllWindows()