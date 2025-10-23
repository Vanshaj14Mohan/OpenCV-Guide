# In this part we will learn about masking using OpenCV.
# Masking is a technique used to focus on a specific part of an image while ignoring the rest.
# A mask is typically a binary image where the area of interest is white (255) and the rest is black (0).

import cv2
import numpy as np

img = cv2.imread("Section Two\Part Two\BigCat_Image.jpg")

cv2.imshow("Original Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()