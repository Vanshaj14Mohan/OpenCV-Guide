# So in this lecture we will learn about gradients and edge detection in OpenCV.
# Gradients are basically the change in intensity or color values in an image.
# They are used to detect edges and transitions in images.

import cv2

img = cv2.imread("Section Two\Part Three\BigCat_Image.jpg")

cv2.imshow("Original Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()