#This is the classifier that returns an image quality
import matplotlib.image as img
import cv2
import numpy as np
import math
import sys
import sklearn as sk
import brisque as b
import os

image = []
score = []

#open all the images in the directory
def parse_images():
    f =  open('paths.txt', 'r')
    data = f.read()
    for file in data:
        image.append(img.imread(file))

def path_walk(folder_path):
    f = []
    file_list = []

    for(dirpath, _, filenames) in os.walk(folder_path):
        for f in filenames:
            file_list.append(os.path.abspath(os.path.join(dirpath, f)))

    f = open('paths.txt', 'w')
    for fl in file_list:
        f.write(fl)
        f.write('\n')
    f.close()


# #feature extraction
# def find_features():


# #train classifier
# def train_it():


#get score for measurable quality difference
def evaluate_quality(paths):
    path_walk(paths)
    parse_images()
    if not images:
        return []
    for i in image:
        score.append(b.test_measure_BRISQUE(image[i]))
    return score


#main
if __name__ == '__main__'