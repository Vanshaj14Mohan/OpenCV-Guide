# So in this lecture we will learn about gradients and edge detection in OpenCV.
# Gradients are basically the change in intensity or color values in an image.
# They are used to detect edges and transitions in images.

import cv2
import numpy as np

img = cv2.imread("Section Two\Part Three\BigCat_Image.jpg")

cv2.imshow("Original Image", img)

#Converting into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayScale Image", gray)

# Using Laplacian Gradient
laplacian = cv2.Laplacian(gray, cv2.CV_64F) # Using CV_64F to avoid overflow and negative values as Laplacian can produce negative values
lap = np.uint8(np.absolute(laplacian)) # Converting back to uint8 as images are usually in this format
cv2.imshow("Laplacian Gradient", lap) # Displaying Laplacian Gradient

# Using Sobel Gradient
# Sobel computes the gradient in both x and y directions separately and then we can combine them

cv2.waitKey(0)
cv2.destroyAllWindows()