# In this part we will learn about thresholding in OpenCV, 
# Thresholding is basically a binary realisation of an image.

import cv2

img = cv2.imread("Section Two\Part Three\BigCat_Image.jpg")

cv2.imshow("Original Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()