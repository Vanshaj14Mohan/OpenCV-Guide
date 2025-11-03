# In this part we will learn about thresholding in OpenCV, 
# Thresholding is basically a binary realisation of an image.
# That is we take an image and convert it into a binary image, pixels are basically 0(Black), 255(White).

import cv2 

img = cv2.imread("Section Two\Part Three\BigCat_Image.jpg")

cv2.imshow("Original Image", img)

# Starting with simple thresholding, converting bgr into grayscale first
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayScale Image", gray)

threshold, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY) # Try changing the threshold value passed as parameter.
cv2.imshow("Simple Threshold", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
