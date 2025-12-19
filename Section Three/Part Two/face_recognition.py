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