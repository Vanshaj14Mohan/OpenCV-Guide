# In this part we will learn about histograms using OpenCV.
# A histogram is a graphical representation of the distribution of pixel intensities in an image.
# It shows how many pixels are present for each intensity value (0-255 for grayscale images).
# We can use histograms to analyze the contrast, brightness, and intensity distribution of an image.
# Can use it  for image equalization and thresholding.

import cv2

img = cv2.imread("Section Two\Part Three\BigCat_Image.jpg")
cv2.imshow("Original Image", img)

# Converting to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()