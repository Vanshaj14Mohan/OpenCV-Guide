# In this we will be building a face recognition system using system using OpenCV's built-in recognizer. 
# We will be using LBPH (Local Binary Patterns Histograms) Face Recognizer for this purpose.
import os
import cv2
import numpy as np 

people = ["Barack Obama", "Sundar Pichai", "Elon Musk", "Tom Cruise", "Michael Jackson"] # Number of faces we will perform operations on 

