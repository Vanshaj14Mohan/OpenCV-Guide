# In this script, we will implement a simple face detection using OpenCV's pre-trained Haar Cascade classifier.
import cv2

# Load the pre-trained Haar Cascade classifier for face detection

img = cv2.imread("Section Three\Photos\girl.jpg")

cv2.imshow("Original Image", img)

# Converting image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()