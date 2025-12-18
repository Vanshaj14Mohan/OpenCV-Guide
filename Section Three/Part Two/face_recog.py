# In this we will be building a face recognition system using system using OpenCV's built-in recognizer. 
import os
import cv2
import numpy as np 

people = ["Barack Obama", "Elon Musk", "Michael Jackson" ,"Sundar Pichai","Tom Cruise"] # Number of faces we will perform operations on 

# One way to load images from a directory
# p = []
# for i in os.listdir(r"E:\OpenCV Guide\Section Three\Part Two\Photos"): # Path where all the images are stored
#     p.append(i) # appending all the images present in the directory to the list p

# print(p) # Printing all the images present in the directory

# Now main method to load images and labels for training the recognizer
DIR = r"E:\OpenCV Guide\Section Three\Part Two\haar_face.xml" # Directory where all the images are stored

haar_cascade = cv2.CascadeClassifier(r"E:\OpenCV Guide\Section Three\haar_face.xml")

features = [] # List to store all the face features
labels = []  # List to store all the labels corresponding to the faces

def create_train():
    for person in people:
        path = os.path.join(DIR, person) # Path to each person's folder
        label = people.index(person) # Getting the index of the person in the people list to use as label

        for img in os.listdir(path):
            img_path = os.path.join(path, img) # Full path to the image

            img_array = cv2.imread(img_path) # Reading the image
            gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY) # Converting the image to grayscale

            face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4) # Detecting faces in the image

            for (x,y,w,h) in face_rect:
                faces_roi = gray[y:y+h, x:x+w] # Region of interest i.e the face area
                features.append(faces_roi) # Appending the face region to features list
                labels.append(label) # Appending the corresponding label to labels list

create_train()

print("Training done ------------------")
print(f"Length of the features = {len(features)}")
print(f"Length of the labels = {len(labels)}")

