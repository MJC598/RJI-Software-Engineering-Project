#This is the classifier that returns an image quality
import matplotlib.image as img
import cv2
import numpy as np
import math
import sys
import sklearn as sk

image = []

#open all the images in the directory
f =  open('paths.txt', 'r')
data = f.read()
for file in data:
    image.append(img.imread(file))


#feature extraction
def find_features():


#train classifier
def train_it():


#get score for measurable quality difference
def 

#run classifier
def run(classifier):

#main
if __name__ == '__main__'