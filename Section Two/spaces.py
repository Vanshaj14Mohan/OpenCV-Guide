# In this part we will learn how to switch between color spaces in OpenCV, A color spaces is basically a space of colors
# Or we can say a system of representing an array of pixel colors.
# Some of the most common color spaces are: BGR, RGB, HSV, LAB, Grayscale etc.
# Each color space has its own advantages and disadvantages, and is used for different purposes in image processing and computer vision tasks.

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Section Two\BigCat_Image.jpg")

cv2.imshow("Original Image", img)

# Converting the image to different color spaces
#1: BGR to Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", gray)

#NOTE: When converting to grayscale, the resulting image has only one channel instead of three. 
# This is because grayscale images represent intensity values, not color information.
# And you cannot convert a grayscale image back to a color image without losing information.
# Also you cannot convert a grayscale image to other color spaces like HSV, LAB, etc. directly.
# You need to convert it back to BGR first, and then to the desired color space.

#2: BGR to HSV (Hue, Saturation, Value)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV Image", hsv)

#3: BGR to LAB (Lightness, A channel, B channel) l*a*b
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow("LAB Image", lab)

#4: BGR to RGB
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("RGB Image", rgb)

plt.imshow(rgb) # Since plt.imshow() expects the image in RGB format, we pass the rgb image here
plt.show() # Would give result in RGB format

#5: BGR to YUV (Y channel, U channel, V channel)
yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
cv2.imshow("YUV Image", yuv)

#6: HSV to BGR
hsv_bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
cv2.imshow("HSV to BGR Image", hsv_bgr)

#7: LAB to BGR
lab_bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
cv2.imshow("LAB to BGR Image", lab_bgr)


cv2.waitKey(0)
cv2.destroyAllWindows()





