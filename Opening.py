import cv2
import numpy as np

logo=cv2.imread("logo.jpg", 0 )
cv2.imshow("Original", logo)
cv2.waitKey(0)


kernel= np.ones((5,5),dtype=np.uint8)


whiteNoise= np.random.randint(0,2,size=logo.shape[:2])
whiteNoise= whiteNoise*255
noise_logo= whiteNoise + logo


opening= cv2.morphologyEx(noise_logo.astype(np.float32),cv2.MORPH_OPEN,kernel)
cv2.imshow("Opening", opening)
cv2.waitKey(0)