import cv2 
import numpy as np

img = cv2.imread("Section One\Part Two\Cat_image.jpg")

# Creating a blank image
blank_image = np.zeros((650, 500, 3), dtype='uint8')
cv2.imshow("Blank Image", blank_image)

# 1:Giving the blank image a color (Blue, Green, Red)
# blank_image[:] = 255, 0, 0 # Blue Color
blank_image[:] = 0, 255, 0 # Green Color
cv2.imshow("Color Image", blank_image)

# 2: Drawing a certain portion of the image
blank_image[200:300, 300:400] = 0,0,255 # Red Color
cv2.imshow("Portion Color Image", blank_image)

# 3: Drawing a Reactangle
cv2.rectangle(blank_image, (0,0), (250, 350), (250,0,0), 2) # Blue Rectangle, cv2.FILLED for filled rectangle
cv2.imshow("Rectangle", blank_image)

# cv2.imshow("Cat Image", img)
# cv2.imshow("Blank Image", blank_image)
cv2.waitKey(0)
