import cv2
import numpy as np

logo=cv2.imread("logo.jpg", 0)
cv2.imshow("Original",logo)
cv2.waitKey(0)

kernel=np.ones((5,5),dtype=np.uint8)

gradient= cv2.morphologyEx(logo,cv2.MORPH_GRADIENT,kernel)
cv2.imshow("Gradient", gradient)
cv2.waitKey(0)