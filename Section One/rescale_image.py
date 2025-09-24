# In this we will learn about how to resize and rescale images using OpenCV
import cv2

img = cv2.imread("Section One\Cat_image.jpg")
cv2.imshow("Cat", img)

# This function will work for images, videos and live videos
def rescaleFrame(frame, scale = 0.75): # To 75% of the original size
    # This function is for rescaling images, videos and live videos
    width = int( frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

resized_image = rescaleFrame(img, scale=0.5) # Rescaling to 50% of the original size
cv2.imshow("Resized Cat", resized_image)

cv2.waitKey(0) 