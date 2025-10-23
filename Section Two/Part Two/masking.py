# In this part we will learn about masking using OpenCV.
# Masking is a technique used to focus on a specific part of an image while ignoring the rest.
# A mask is typically a binary image where the area of interest is white (255) and the rest is black (0).
# Dimesions of the mask should be the same as the original image for proper masking.

import cv2
import numpy as np

img = cv2.imread("Section Two\Part Two\BigCat_Image.jpg")
cv2.imshow("Original Image", img)

blank = np.zeros(img.shape[:2], dtype="uint8") # Creating a blank mask with same height and width as original image
cv2.imshow("Blank Image", blank)

# Creating a circular mask
mask = cv2.circle(blank, (img.shape[1]//2 + 35, img.shape[0]//2), 100, 255, -1) # Creating a circular mask
cv2.imshow("Mask", mask)

#Extra code------
circle_mask = cv2.circle(blank.copy(), (img.shape[1]//2 + 35, img.shape[0]//2), 100, 255, -1) # Creating a circular mask
cv2.imshow("Mask", circle_mask)

rectangle = cv2.rectangle(blank.copy(), (40,40), (380,380), 255, -1)

weird_mask = cv2.bitwise_xor(circle_mask, rectangle)
cv2.imshow("Wierd Mask", weird_mask)
# ---------------- Extra Code ends here

# Creating a rectangular mask
rect_mask = cv2.rectangle(blank, (img.shape[1]//2, img.shape[0]//2),(img.shape[1]//2 + 90, img.shape[0]//2 + 90) ,100, 255, -1) # Creating a circular mask

# Now creating a masked image using bitwise AND operation
masked_img = cv2.bitwise_and(img, img, mask=mask) # Applying the mask to the original image
cv2.imshow("Masked Image", masked_img)

cv2.waitKey(0)
cv2.destroyAllWindows()