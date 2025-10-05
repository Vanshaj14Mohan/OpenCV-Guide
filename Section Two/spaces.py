# In this part we will learn how to switch between color spaces in OpenCV, A color spaces is basically a space of colors
# Or we can say a system of representing an array of pixel colors.
# Some of the most common color spaces are: BGR, RGB, HSV, LAB, Grayscale etc.
# Each color space has its own advantages and disadvantages, and is used for different purposes in image processing and computer vision tasks.

import cv2

img = cv2.imread("Section Two\BigCat_Image.jpg")

cv2.imshow("Original Image", img)

# Converting the image to different color spaces
#1: BGR to Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", gray)

#2: BGR to HSV (Hue, Saturation, Value)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV Image", hsv)

#3: BGR to LAB (Lightness, A channel, B channel) l*a*b
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow("LAB Image", lab)

#4: BGR to RGB
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("RGB Image", rgb)

#5: BGR to YUV


cv2.waitKey(0)
cv2.destroyAllWindows()





