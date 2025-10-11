# In this part we will learn how to split and merge image channels using OpenCV.
# Splitting an image means separating the image into its individual color channels.
# Merging an image means combining the individual color channels back into a single image.

import cv2 

img = cv2.imread("Section Two\Part Two\BigCat_Image.jpg")

cv2.imshow("Original Image", img)

b,g,r = cv2.split(img) # Splitting the image into its BGR channels

cv2.imshow("Blue Channel", b)
cv2.imshow("Green Channel", g)
cv2.imshow("Red Channel", r)

# For shapes
print(img.shape) # (height, width, channels)
print(b.shape) # (height, width) --> single channel
print(g.shape) # (height, width)
print(r.shape) # (height, width)

# For merging the channels back to form the original image
merged = cv2.merge([b,g,r])
cv2.imshow("Merged Image", merged)


cv2.waitKey(0)
cv2.destroyAllWindows()
