### What image classifier we used:

For our classifier we decided to drop libsvm and brisque as the difficulties installing the dependencies wasted too much of our time. We instead went with a classifier called Idealo, which we found thanks to the other RJI groups. Idealo works off of Google's NIMA (Neural Image Assessment). It aims to predict the aesthetic quality and the techincal quality of images, which is perfect for what we wanted to do. The models are trained with transfer learning where ImageNet pre-trained CNNs are used to classify the images. 

### Whether or not we have started to build classifiers from Ed's library:

We have started to build a classifier based off of Ed's library, however we've only gotten it working on one image at a time and not a whole directory. We aim to finish the classifier by looping it through a given directory if a directory is sent or just using it on a file if only one image is to be classified. This shouldn't be too large of a problem, but we didn't think the dependencies for brisque would cause an issue, so we'll see.
