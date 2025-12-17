# In this we will be building a face recognition system using system using OpenCV's built-in recognizer. 
# We will be using LBPH (Local Binary Patterns Histograms) Face Recognizer for this purpose.
import os
import cv2
import numpy as np 

people = ["Barack Obama", "Elon Musk", "Michael Jackson" ,"Sundar Pichai","Tom Cruise"] # Number of faces we will perform operations on 

p = []
for i in os.listdir(r"E:\OpenCV Guide\Section Three\Part Two\Photos"): # Path where all the images are stored
    p.append(i) # appending all the images present in the directory to the list p

print(p) # Printing all the images present in the directory