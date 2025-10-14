# In this part we are gonna understand different smoothing and blurring techniques using OpenCV.
# Smoothing is used to reduce noise and improve the quality of an image.

import cv2

img = cv2.imread("Section Two\Part Two\BigCat_Image.jpg")

cv2.imshow("Original Image", img)


cv2.waitKey(0)
cv2.destroyAllWindows()
