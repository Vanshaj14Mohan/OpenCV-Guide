# In this part we will learn about the most basic functions in OpenCV.
import cv2

img = cv2.imread("Section One\Part Two\Cat_image.jpg")

cv2.imshow("Cat Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()