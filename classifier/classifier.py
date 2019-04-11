#This is the big boy classifier that returns an image quality
import matplotlib.image as img

image = []

f =  open('paths.txt', 'r')
data = f.read()
for file in data:
    image.append(img.imread(file))

