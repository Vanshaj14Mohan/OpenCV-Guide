# In this we will learn about bitwise operations using OpenCV.
# Bitwise operations are used to manipulate binary images. Especially useful in masking operations.
# At a very high level, these operations work on the binary representation of the pixel values. that is 0s and 1s.
# There are four types of bitwise operations: AND, OR, NOT, XOR.
import cv2
import numpy as np

# Creating binary images, 400x400 pixels and drawing a rectangle and a circle
blank = np.zeros((400,400), dtype="uint8")

rectangle = cv2.rectangle(blank.copy(), (40,40), (380,380), 255, -1) # white rectangle, -1 fills the shape
circle = cv2.circle(blank.copy(), (200,200), 200, 255, -1) # white circle

cv2.imshow("Rectangle", rectangle)
cv2.imshow("Circle", circle)

#bitwise AND, the output is white only where both images are white, else black and it returns a new image
bitwise_and = cv2.bitwise_and(rectangle, circle)
cv2.imshow("Bitwise AND", bitwise_and)

#bitwise OR, the output is white where at least one image is white, else black and it returns a new image
bitwise_or = cv2.bitwise_or(rectangle, circle)
cv2.imshow("Bitwise OR", bitwise_or)

cv2.waitKey(0)
cv2.destroyAllWindows()
