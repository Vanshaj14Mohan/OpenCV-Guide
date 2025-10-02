import cv2 
import numpy as np

img = cv2.imread("Section One\Part Two\Cat_image.jpg")

# Creating a blank image
blank_image = np.zeros((650, 500, 3), dtype='uint8') # (Height, Width, Color_Channel) & each pixel value is an 8-bit integer (0–255 range)
cv2.imshow("Blank Image", blank_image)

# 1:Giving the blank image a color (Blue, Green, Red)
# blank_image[:] = 255, 0, 0 # Blue Color
blank_image[:] = 0, 255, 0 # Green Color
cv2.imshow("Color Image", blank_image)

# 2: Drawing a certain portion of the image
blank_image[200:300, 300:400] = 0,0,255 # Red Color
cv2.imshow("Portion Color Image", blank_image)

# 3: Drawing a Rectangle
cv2.rectangle(blank_image, (0,0), (250, 350), (250,0,0), 2) # Blue Rectangle, cv2.FILLED for filled rectangle instead of thickeness
cv2.imshow("Rectangle", blank_image)

# 4: Drawing a Circle
cv2.circle(blank_image, (400,100), 30, (255, 0, 0), -1) # Blue Circle, -1 for filled circle
cv2.imshow("Circle", blank_image)

# 5: Drawing a Line
cv2.line(blank_image, (100,100), (250, 400), (255, 255, 255), 3) # White Line
cv2.imshow("White Line", blank_image)

# 6: Putting Text on the Image
cv2.putText(blank_image, "Computer Vision", (200,500), cv2.FONT_HERSHEY_COMPLEX, 1.0, (255,0,0), 2) # Blue Text
cv2.imshow("Text on Image", blank_image)

# cv2.imshow("Cat Image", img)
# cv2.imshow("Blank Image", blank_image)
cv2.waitKey(0)
