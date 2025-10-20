# In this part we are gonna understand different smoothing and blurring techniques using OpenCV.
# Smoothing is used to reduce noise and improve the quality of an image.
# Blurring is a type of smoothing that reduces the sharpness of an image.
# There are different types of blurring techniques like average blurring, Gaussian blurring, median blurring, bilateral filtering etc.

import cv2

img = cv2.imread("Section Two\Part Two\BigCat_Image.jpg")

# cv2.imshow("Original Image", img)

#1: Average Blurring
# It takes the average of all the pixels under the kernel area and replaces the central element with this average.
average = cv2.blur(img, (3,3)) # (3,3) is the kernel size
cv2.imshow("Average Blurring", average)
# Note: The kernel size should be odd and positive. eg (3,3), (5,5), (7,7) etc.
# A larger kernel size means more blurring.
# A smaller kernel size means less blurring.
# Average blurring is not very effective in removing noise.
# It is better to use Gaussian blurring or median blurring for better results.

#2: Gaussian Blurring
# It takes the weighted average of all the pixels under the kernel area and replaces the central element
# with this weighted average. The weights are calculated using a Gaussian function.
gaussian = cv2.GaussianBlur(img, (3,3), 0) # (3,3) is the kernel size, 0 is the standard deviation in X direction
cv2.imshow("Gaussian Blurring", gaussian)

#3: Median Blurring
# Same as average blurring but instead of taking the average, it takes the median.
# It takes the median of all the pixels under the kernel area and replaces the central element with this median.
# Generally it tends to be more effective in reducing noise in any image as compared to Average and Gaussian method
median = cv2.medianBlur(img, 3) # 3 is the kernel size, it should be odd and positive, only one value is needed 
cv2.imshow("Median Blurring", median)

#4: Bilateral Filtering/Blurring
# It is very effective in noise removal while keeping edges sharp. Sometimes used in advanced image processing.
# It takes the weighted average of all the pixels under the kernel area and replaces the central element.
bilateral = cv2.bilateralFilter(img, 10, 15, 15) # 10 is the diameter of each pixel neighborhood, 15 is sigmaColor, 15 is sigmaSpace
cv2.imshow("Bilateral Blurring", bilateral) 

cv2.waitKey(0)
cv2.destroyAllWindows()
