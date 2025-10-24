# In this part we will learn about histograms using OpenCV.
# A histogram is a graphical representation of the distribution of pixel intensities in an image.
# It shows how many pixels are present for each intensity value (0-255 for grayscale images).
# We can use histograms to analyze the contrast, brightness, and intensity distribution of an image.
# Can use it  for image equalization and thresholding.

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Section Two\Part Three\BigCat_Image.jpg")
cv2.imshow("Original Image", img)

# Drawing a mask to focus on a specific region
blank = np.zeros(img.shape[:2], dtype="uint8") # Creating a blank mask with same height and width as original image

# Converting to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", gray)

# Creating a circular mask
circle= cv2.circle(blank, (img.shape[1]//2 + 35, img.shape[0]//2), 100, 255, -1) # Creating a circular mask
mask = cv2.bitwise_and(gray, gray, mask=circle) # Applying the mask to the grayscale image
cv2.imshow("Masked Grayscale Image", mask)

# Computing grayscale histogram, the images are passed in a list, then channel number (0 for grayscale), 
# mask (None for full image), histogram size (256 bins), range of pixel values (0-256)
# gray_hist = cv2.calcHist([gray], [0], None, [256], [0,256])
gray_hist = cv2.calcHist([gray], [0], mask, [256], [0,256])

# Plotting the grayscale histogram
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("Number of Pixels")
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()