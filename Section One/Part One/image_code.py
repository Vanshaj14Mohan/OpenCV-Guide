# For Image Display
import cv2

img = cv2.imread("Section One\Part One\Cat_image.jpg")

cv2.imshow("Cat", img) # Displaying the image in a window
cv2.waitKey(0) # Waits indefinitely until a key is pressed
cv2.destroyAllWindows() # Closes all the windows opened by OpenCV
