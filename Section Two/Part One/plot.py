#Note: OpenCV uses BGR color space by default, while many other libraries use RGB color space. 
# So, when working with images in OpenCV, it's important to keep this in mind and convert between 
# color spaces as needed.BGR to RGB.
#Outside of OpenCV, RGB is the most commonly used color space.

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Section Two\Part One\BigCat_Image.jpg")
cv2.imshow("Original Image", img)

plt.imshow(img)
plt.show() # Would give result in RGB format

cv2.waitKey(0)
cv2.destroyAllWindows()
