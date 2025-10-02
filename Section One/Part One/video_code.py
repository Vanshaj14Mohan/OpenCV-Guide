# For Video Display
import cv2

capture = cv2.VideoCapture(r"Section One\Part One\SmallCat_Video.mp4")

while True:
    isTrue, frame = capture.read()
    if not isTrue: # Break the loop if there are no more frames to read
        break
    cv2.imshow("Video", frame)
    if cv2.waitKey(20) & 0xFF==ord("q"): # Press 'q' to quit
        break

capture.release()
cv2.destroyAllWindows()