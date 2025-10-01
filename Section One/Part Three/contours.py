# In this part we will learn how to find contours in an image using OpenCV.
# Contours can be explained simply as a curve joining all the continuous points (along the boundary), 
# having same color or intensity.
# Contours are a useful tool for shape analysis and object detection and recognition.

import cv2
import numpy as np

img = cv2.imread("Section One\Part Three\Cat_image.jpg")

cv2.imshow("Original Image", img)

blank = np.zeros(img.shape, dtype="uint8") # Creating a blank image
cv2.imshow("Blank Image", blank) # we will use this blank image to draw contours on it.

# Convert to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", gray_img)

# Blurring the image
blur = cv2.GaussianBlur(gray_img, (7,7), cv2.BORDER_DEFAULT)
cv2.imshow("Blur Image", blur)

# # Creating an edge cascade
canny = cv2.Canny(img, 120, 170) # Passing blurred image to canny would give better results. Can try that too..
cv2.imshow("Canny Edge Image", canny) 

#Another way to get contours we can use another function called threshold 
ret, thresh = cv2.threshold(gray_img, 125,255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Image", thresh) # Threshold image is a binary image (ie only black and white)

# Finding Contours
# By using, cv2.findContours() function takes three arguments, the first is the source image, 
# the second is the contour retrieval mode, and the third is the contour approximation method.
# It returns the contours and the hierarchy.

contours, heirarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(f"{len(contours)} contours found!") # Passing canny image to find contours would reduce the number of contours found.
#----------------------------------
# cv2.RETR_LIST --> retrieves all of the contours without establishing any hierarchical relationships.
# cv2.RETR_EXTERNAL --> retrieves only the extreme outer contours.
# cv2.RETR_TREE --> retrieves all of the contours and reconstructs a full hierarchy of nested contours.
# cv2.CHAIN_APPROX_NONE --> stores all the contour points (ie all the boundary points).
# cv2.CHAIN_APPROX_SIMPLE --> removes all redundant points and compresses the contour, thereby saving memory.
#----------------------------------
#----------------------------------
# Contours is a Python list of all the contours in the image.
# Each individual contour is a Numpy array of (x,y) coordinates of boundary points of the object.
# Heirarchy contains information about the image topology.
# It has as many elements as the number of contours.
# cv2.RETR_LIST retrieves all of the contours without establishing any hierarchical relationships.
# cv2.CHAIN_APPROX_NONE stores all the contour points.
#----------------------------------

cv2.drawContours(blank, contours, -1, (0,255,0), 1) # Drawing all contours on the blank image. -1 means drawing all contours. We can also specify index of contour to draw that specific contour.
cv2.imshow("Contours Drawn", blank)

cv2.waitKey(0)
cv2.destroyAllWindows()
