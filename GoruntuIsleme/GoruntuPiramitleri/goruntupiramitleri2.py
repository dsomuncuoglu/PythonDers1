import cv2
import numpy as np


image=np.zeros((300,300,3),dtype="uint8")

print(image)

#cv2.imshow("Array",image)

cv2.waitKey(0)
cv2.destroyAllWindows()