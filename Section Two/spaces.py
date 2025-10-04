# In this part we will learn how to switch between color spaces in OpenCV, A color spaces is basically a space of colors
# Or we can say a system of representing an array of pixel colors.
# Some of the most common color spaces are: BGR, RGB, HSV, LAB, Grayscale etc.
# Each color space has its own advantages and disadvantages, and is used for different purposes in image processing and computer vision tasks.

import cv2

img = cv2.imread("Section Two\Cat_Image.jpg")

cv2.imshow("Original Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()




