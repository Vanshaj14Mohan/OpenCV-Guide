# In this part we will learn how to find contours in an image using OpenCV.
# Contours can be explained simply as a curve joining all the continuous points (along the boundary), 
# having same color or intensity.
# Contours are a useful tool for shape analysis and object detection and recognition.

import cv2

img = cv2.imread("Section One\Part Three\Cat_image.jpg")

cv2.imshow("Original Image", img)

# Convert to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", gray_img)

# Creating an edge cascade
canny = cv2.Canny(gray_img, 120, 170)
cv2.imshow("Canny Edge Image", canny)

# Finding Contours
# By using, cv2.findContours() function takes three arguments, the first is the source image, 
# the second is the contour retrieval mode, and the third is the contour approximation method.
# It returns the contours and the hierarchy.

contours, heirarchy = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print(f"{len(contours)} contours found!")
#----------------------------------
# cv2.RETR_LIST --> retrieves all of the contours without establishing any hierarchical relationships.
# cv2.RETR_EXTERNAL --> retrieves only the extreme outer contours.
# cv2.RETR_TREE --> retrieves all of the contours and reconstructs a full hierarchy of nested contours.
# cv2.CHAIN_APPROX_NONE --> stores all the contour points (ie all the boundary points).
# cv2.CHAIN_APPROX_SIMPLE --> removes all redundant points and compresses the contour, thereby saving memory.
#----------------------------------
# Contours is a Python list of all the contours in the image.
# Each individual contour is a Numpy array of (x,y) coordinates of boundary points of the object.
# Heirarchy contains information about the image topology.
# It has as many elements as the number of contours.
# cv2.RETR_LIST retrieves all of the contours without establishing any hierarchical relationships.
# cv2.CHAIN_APPROX_NONE stores all the contour points.

cv2.waitKey(0)
cv2.destroyAllWindows()
