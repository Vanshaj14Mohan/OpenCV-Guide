# In this part we will learn about histograms using OpenCV.
# A histogram is a graphical representation of the distribution of pixel intensities in an image.
# It shows how many pixels are present for each intensity value (0-255 for grayscale images).
# We can use histograms to analyze the contrast, brightness, and intensity distribution of an image.
# Can use it  for image equalization and thresholding.

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Section Two\Part Three\BigCat_Image.jpg")
cv2.imshow("Original Image", img)

# Converting to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", gray)

# Computing grayscale histogram, the images are passed in a list, then channel number (0 for grayscale), 
# mask (None for full image), histogram size (256 bins), range of pixel values (0-256)
gray_hist = cv2.calcHist([gray], [0], None, [256], [0,256])

# Plotting the grayscale histogram
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()