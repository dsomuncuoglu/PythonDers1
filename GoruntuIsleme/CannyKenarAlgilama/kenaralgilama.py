import cv2
import numpy as np

image=cv2.imread("money.png")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(3,3),0)
widecanny=cv2.Canny(blur,10,220)
tightcanny=cv2.Canny(blur,200,230)

def AutoCanny(blur,sigma=0.33):
    median=np.median(blur)
    lower=int(max(0,(1.0-sigma)*median))
    upper=int(min(255,(1.0-sigma)*median))
    canny2=cv2.Canny(blur,lower,upper)
    return canny2

auto=AutoCanny(blur)


cv2.imshow("Orjinal",image)
cv2.imshow("Blur and gray",blur)
cv2.imshow("Wide Canny",widecanny)
cv2.imshow("Tight Canny",tightcanny)
cv2.imshow("Auto Canny",auto)
cv2.imshow("Edges",np.hstack([widecanny,tightcanny,auto]))


cv2.waitKey(0)
cv2.destroyAllWindows()
