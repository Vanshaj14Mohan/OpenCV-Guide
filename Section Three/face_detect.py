# In this script, we will implement a simple face detection using OpenCV's pre-trained Haar Cascade classifier.
import cv2

# Load the pre-trained Haar Cascade classifier for face detection

img = cv2.imread("Section Three\Photos\group 1.jpg")

cv2.imshow("Original Image", img)

# Converting image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", gray)

# Creating the haar cascade object
haar_cascade = cv2.CascadeClassifier(r"E:\OpenCV Guide\Section Three\haar_face.xml") # Make sure the haar_face.xml file is in the same directory as this script
# this will detect faces, CascadeClassifier is a class in cv2 which loads the xml file

face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1) # Detecting faces, detectMultiScale is a method in CascadeClassifier class
# Draw rectangle around the faces that is why face_rect is used in for loop
#scaleFactor: Parameter specifying how much the image size is reduced at each image scale.
#minNeighbors: Parameter specifying how many neighbors each candidate rectangle should have to retain it.

print(f"Number of faces found = {len(face_rect)}")

for(x,y,w,h) in face_rect:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv2.imshow("Detected Faces", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Note: Haar Cascades are not the most accurate method for face detection,
# but they are fast and work well for simple applications. For more robust face detection, 
# consider using deep learning-based methods.

# dilib face detector is more accurate than haar cascade but haar cascade is faster than dlib face detector.
# It is less sensitive to noise and can detect faces at different scales and orientations.