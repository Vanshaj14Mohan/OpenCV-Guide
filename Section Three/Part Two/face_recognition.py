import numpy as np
import cv2

people = ["Barack Obama", "Elon Musk", "Michael Jackson" ,"Sundar Pichai","Tom Cruise"] # Number of faces we will perform operations on 

haar_cascade = cv2.CascadeClassifier(r"E:\OpenCV Guide\Section Three\Part Two\haar_face.xml") # Loading the haar cascade classifier

# Loding features and labels arrays
features = np.load("features.npy", allow_pickle=True) # allow_pickle=True to load arrays of different sizes
labels = np.load("labels.npy")

face_recognizer = cv2.face.LBPHFaceRecognizer_create() # Creating the LBPH Face Recognizer,
#LBPH = Local Binary Patterns Histograms, which is effective for face recognition tasks helps in recognizing faces under varying lighting conditions.
face_recognizer.read("face_trained.yml") # Loading the trained model

img = cv2.imread(r"E:\OpenCV Guide\Section Three\Part Two\Photos\Tom Cruise\tom-cruise 6.jpg") # Reading the test image
# Once done we will test the recognizer on a new image

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Converting the image to grayscale
cv2.imshow("Person", gray)

# detecting faces in the image
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w] # Region of interest i.e the face area

    label, confidence = face_recognizer.predict(faces_roi) # Predicting the label and confidence for the detected face
    print(f"Label = {people[label]} with a confidence of {confidence}") # Printing the label and confidence

    cv2.putText(img, str(people[label]), (20,20), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2) # Putting the predicted label on the image
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2) # Drawing rectangle around the face

cv2.imshow("Detected Face", img) # Displaying the image with detected face and label
cv2.waitKey(0)
