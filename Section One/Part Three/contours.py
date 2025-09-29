# In this part we will learn how to find contours in an image using OpenCV.
# Contours can be explained simply as a curve joining all the continuous points (along the boundary), 
# having same color or intensity.
# Contours are a useful tool for shape analysis and object detection and recognition.

import cv2

img = cv2.imread("Section One\Part Three\Cat_image.jpg")

cv2.imshow("Original Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
