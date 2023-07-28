import cv2
import numpy as np

logo=cv2.imread("logo.jpg", 0)

cv2.imshow("Original", logo )
cv2.waitKey(0)

kernel= np.ones((5,5),dtype=np.uint8)

result= cv2.erode(logo,kernel,iterations=1)

cv2.imshow("Erozyon", result )
cv2.waitKey(0)

