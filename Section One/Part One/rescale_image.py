# In this we will learn about how to resize and rescale images using OpenCV
import cv2

img = cv2.imread("Section One\Part One\Cat_image.jpg")
cv2.imshow("Cat", img)

# This function will work for images, videos and live videos
def rescaleFrame(frame, scale = 0.75): # To 75% of the original size
    # This function is for rescaling images, videos and live videos
    # Calculate the new width (original width * scale factor)
    width = int( frame.shape[1] * scale) # shape[1] is width 

    # Calculate the new height (original height * scale factor)
    height = int(frame.shape[0] * scale) # shape[0] is height 
    dimensions = (width, height) # Create a tuple of new dimensions (width, height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA) # Resize the frame to the new dimensions using INTER_AREA interpolation
    # cv2.INTER_AREA is recommended for shrinking images

resized_image = rescaleFrame(img, scale=0.5) # Rescaling to 50% of the original size
cv2.imshow("Resized Cat", resized_image)
cv2.waitKey(0) 
cv2.destroyAllWindows()