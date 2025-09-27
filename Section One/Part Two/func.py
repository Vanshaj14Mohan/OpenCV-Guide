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

#3: Creating an edge cascade
canny = cv2.Canny(img, 125, 175)
cv2.imshow("Canny Image", canny)

#4: Dilating the image using specific structuring element(ie using Canny image)
dilated = cv2.dilate(canny, (7,7), iterations = 3)
cv2.imshow("Dilated Image", dilated)

#5: Eroding the image using specific structuring element(ie using Dilated image)
eroded = cv2.erode(dilated, (5,5), iterations=3)
cv2.imshow("Eroded Image", eroded)

#6: Resizing the image
resized = cv2.resize(img, (500, 500), interpolation=cv2.INTER_CUBIC)
cv2.imshow("Resized Image", resized)

#7: Cropping the image
cropped = img[0:400, 0:500]
cv2.imshow("Cropped Image", cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()