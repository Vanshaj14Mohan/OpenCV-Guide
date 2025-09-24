# In this we will learn about how to resize and rescale frames using OpenCV
# For this we will use cv2.resize() function
# Starting from videos and then we will move to images and live videos
import cv2

def rescaleFrame(frame, scale = 0.75): # To 75% of the original size
    # This function is for rescaling images, videos and live videos
    width = int( frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

def Changeres(width,height):
    # This function is for live videos
    capture.set(3, width) # 3 is for width
    capture.set(4, height) # 4 is for height

#For reading videos
capture = cv2.VideoCapture(r"Section One\Part One\SmallCat_Video.mp4")

while True:
    isTrue, frame = capture.read()

    if not isTrue: # If there are no frames left to read, then break
        break

    frame_resized = rescaleFrame(frame, scale=0.3) # Rescaling to 40% of the original size
    cv2.imshow("Video", frame)
    cv2.imshow("Video Resized", frame_resized)
    if cv2.waitKey(20) & 0xFF==ord("q"): # Press 'q' to quit
        break

capture.release()
cv2.destroyAllWindows()
