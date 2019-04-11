#this will connect the classifier to the dataset (likely in flask) and have premade queries written
import os
import cv2

#read in a literal string path name
path = input()
#build a list of each of the contents of the path
dir_content = os.listdir(path)

img_list = [];
#for each item in the list read in the image and store to img_list
for name in dir_content:
    img_list.append(cv2.imread(name))

