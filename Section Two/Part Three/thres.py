# In this part we will learn about thresholding in OpenCV, 
# Thresholding is basically a binary realisation of an image.
# That is we take an image and convert it into a binary image, pixels are basically 0(Black), 255(White).

import cv2 

img = cv2.imread("Section Two\Part Three\BigCat_Image.jpg")

cv2.imshow("Original Image", img)

# Starting with simple thresholding, converting bgr into grayscale first 
# So in simple thresholding, we have to set a fixed threshold value.
# All the pixel values above that threshold value will be set to white(255) and all the pixel values below that threshold value will be set to black(0).
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayScale Image", gray)

threshold, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY) # Try changing the threshold value passed as parameter.
cv2.imshow("Simple Threshold", thresh)

# Adaptive Thresholding
# In simple thresholding we have to set a fixed threshold value, but in adaptive thresholding
# the threshold value is calculated for smaller regions of the image. This helps in getting better results for images with varying illumination.
adaptive_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2) # we can also use cv2.ADAPTIVE_THRESH_GAUSSIAN_C instead of cv2.ADAPTIVE_THRESH_MEAN_C
cv2.imshow("Adaptive Threshold", adaptive_thresh)
# so in adaptive thresholding, 11 is the block size (size of the neighborhood area) and 3 is the constant subtracted from the mean.

# we can also create inverse threshold as well
threshold, thresh_inv = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV) # Binary Inverse
cv2.imshow("Inverse Threshold", thresh_inv) # all black part converts into white and all white part converts into black.

cv2.waitKey(0)
cv2.destroyAllWindows()
