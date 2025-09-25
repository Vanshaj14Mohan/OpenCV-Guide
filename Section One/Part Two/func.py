# In this part we will learn about the most basic functions in OpenCV.
import cv2

img = cv2.imread("Section One\Part Two\Cat_image.jpg")

cv2.imshow("Cat Image", img) 

#1: Converting the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", gray)

#2: Blurring the image
blur = cv2.GaussianBlur(img, (7,7), cv2.BORDER_DEFAULT)
cv2.imshow("Blur Image", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()