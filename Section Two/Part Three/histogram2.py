# Now computing color histogram for each channel (BGR)
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Section Two\Part Three\BigCat_Image.jpg")
cv2.imshow("Original Image", img)

# Drawing a mask to focus on a specific region
blank = np.zeros(img.shape[:2], dtype="uint8") # Creating a blank mask with same height and width as original image

# Creating a circular mask
mask= cv2.circle(blank, (img.shape[1]//2 + 35, img.shape[0]//2), 100, 255, -1) # Creating a circular mask, gave it name mask to avoid confusion with grayscale mask
masked = cv2.bitwise_and(img, img, mask=mask) # Applying the mask to the grayscale image
cv2.imshow("Masked Color Image", masked)

# Computing color histogram for each channel (BGR)
colors = ("b", "g", "r") # Defining color channels using tuples created by OpenCV

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("Number of Pixels")
for i, col in enumerate(colors):
    hist = cv2.calcHist([img], [i], mask, [256], [0,256]) # Calculating histogram for each channel
    plt.plot(hist, color=col) # Plotting histogram with respective color
    plt.xlim([0,256])
    plt.title("Color Histogram") 
    # plt.xlabel("Bins")
    # plt.ylabel("Number of Pixels")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()