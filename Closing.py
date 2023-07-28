import cv2
import numpy as np

logo = cv2.imread("logo.jpg")
cv2.imshow("original", logo)

logo_gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)

kernel = np.ones((5, 5), dtype=np.uint8)

blackNoise = np.random.randint(0, 2, size=logo.shape[:2])
blackNoise = blackNoise * -255

noise_logo = blackNoise + logo_gray
noise_logo[noise_logo <= 0] = 0

noise_logo = noise_logo.astype(np.uint8)

cv2.imshow("noisy_logo", noise_logo)
cv2.waitKey(0)
cv2.destroyAllWindows()
