# In this part we will learn how to split and merge image channels using OpenCV.
# Splitting an image means separating the image into its individual color channels.
# Merging an image means combining the individual color channels back into a single image.

import cv2 

img = cv2.imread("Section Two\Part Two\BigCat_Image.jpg")

cv2.imshow("Original Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
