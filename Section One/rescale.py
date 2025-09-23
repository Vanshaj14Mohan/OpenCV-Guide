# In this we will learn about how to resize and rescale frames using OpenCV

import cv2

def rescaleFrame(frame, scale = 0.75): # To 75% of the original size
    # This function is for rescaling images, videos and live videos
    width = int( frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)