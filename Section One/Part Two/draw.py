import cv2 
import numpy as np

img = cv2.imread("Section One\Part Two\Cat_image.jpg")

# Creating a blank image
blank_image = np.zeros((650, 500, 3), dtype='uint8')

cv2.imshow("Cat Image", img)
cv2.imshow("Blank Image", blank_image)
cv2.waitKey(0)
