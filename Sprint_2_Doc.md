# Sprint 2 Design Document
#### Group 04
#### Matthew Carroll, Dylan Bunch, Olivia Bishop


## Deployment Environment

http://ec2-13-59-146-242.us-east-2.compute.amazonaws.com/

http://ec2-13-59-146-242.us-east-2.compute.amazonaws.com/view_images.php (displays file name along with both technical & aesthetic scores)

## Functional Requirements

1. Load Data
    1. load\_path()
        * Input: User specified path
        * Output: Boolean Value
            * Checks if path supplied is in use already or if pictures can be loaded to that specific location on the server. Returns True if avaliable, False otherwise
        * If false is returned to this function, need to update user that path is already in use
    2. save_folder()
        * Input: image(s), path to save location
        * Output: Boolean Value
        * Attempts to store image(s) at path on server. If it succeeds it returns True, otherwise it returns False.
        * Should be able to be navigated to after data is loaded.
2. View Metadata
    1. get_metadata()
        * Input: Path
        * Output: Gets Metadata off JPEG
        * This is the primary function call to view metadata, it will contain multiple helper functions
    2. find_pic()
        * Input: Path
        * Output: Image
        * Put in path, return picture location on server, primarily a helper function
    2. extract_data()
        * Input: Image
        * Output: Metadata list, unsorted
        * Given an image, this returns all the raw metadata associated with the image. It needs to be sorted
    3. sort_data()
        * Input: Raw Metadata List
        * Output: Metadata dictionary
        * This will return key/value pairs of data in JSON format so that it is easy to pull specific components and format it into a webpage
3. Quality Evaluation
    1. evaluate\_quality()
        * Input: path to image
        * Output: Ranking and tags stored in JPEG metadata on pic, list of ranks returned in picture order
            * Runs on RJI server next to pictures
            * Input supplied by user, output stored in picture data on server
            * If list of ranks is not null, return the list to the user associated with the path
    2. find_features()
        * Input: Test Image dataset in matrix form
        * Output: feature list
        * This function would enable us to actually pass a list of features to have the machine train on and speed up training and testing.
    3. train()
        * Input: Training Image Datasets
        * Output: Trained classifier
        * Train the classifier based on the training image data supplied. This would likely be in the form of a path. This function will likely contain a call to find_features for each of the training image datasets.
        * This is the meat of the class and will take the most computational power.
4. View Images
    1. view\_images()
        * Input: path(s) to pictures
        * Output: Images
        * This is the main function of this use case, it will loop over the get_pic helper function to return all pictures selected.
            * Might be worth adjusting to call it Asynchronously
    2. get_pic()
        * Input: path of a picture
        * Output: Image
        * Takes in one path and makes an API call to return 1 picture from the server.	




## Database Design

#### ERD
![ERD](https://github.com/MJC598/RJI-Software-Engineering-Project/blob/master/Sprint1RJI_ERD.jpg "Sprint1_ERD")


## Visual Design
![Visual Design](https://github.com/MJC598/RJI-Software-Engineering-Project/blob/master/Visual_Design.jpg "Visual_Design")
## Project Direction
We started with the intent of trying to get Quality Evaluation working correctly. We immediately ran into dependency issues that lasted the entire week. We didn't decide till late in the weekend to switch to a focus more towards view_images. We now have a php script that can easily transcribe json files to html tables and a python script that can easily pull data from the server to the json file. It just is not 100% connected because we are still struggling with the dependencies in the quality evaluation, so our data is bad. 

### Completed:

1. API
    * Successfully retrieve information from server given path to a folder of images.
    * Successfully convert these images into useful information, such as [filename,path] and [filename,rating1,rating2] tuples in a json string.
    * Successfully write json strings out to files to be interpreted by the UI.
2. UI
    * Successfully displayed _extremely_ rough page of pulled filenames and test ratings.
3. Classifier
    * Successfully found a classifier able to analyze technical aspects of picture with valid test results.

### To Do:

1. API
    * Connect API to classifier (waiting on finish, technical issues)
2. UI
    * Make homepage look nice
    * Make page for displaying filenames and ratings look presentable
    * Make page for uploading url to rate
3. Classifier
    * Implement technical classifier and locate/build aesthetic classifier and dependencies.

## Files

1. /ui/
    * index.html
        * View Images, View Metadata
        * This is the primary file for the website's design, styling, and functionality
    * view_images.php
        * report data from names_and_ratings.json file output by api.py into an HTML table for user readability
2. /classifier/
    * classification\_db\_connection.py
        * Quality Evaluation, Load Data
        * File description
    * classifier.py
        * Quality Evaluation
        * The classification algorithm is held within this file, to be ran on the RJI server
    * paths.txt
        * View Images, View Metadata, Load Data
        * File that stores the paths of photos from the RJI server for using later
3. /api/
    * api.py
        * Load Data, View Metadata, View Images
        * File that is meant to call functions on the RJI server and on our server to send data back and forth between the two. Essentially the controller.

### Unit Tests:


### Technical Issues:

1. API
    * Issues properly outputting an enormous string of filenames and paths to be json parseable
2. UI
    * No Issues!
3. Classifier
    * Issues getting dependencies to work on ec2 instance (package manager is much more limited than we thought; pip and python versioning problems)
        * libsvm installation failed on opening a shared object file
        * tried setting up a virtual environment to account for both version of python installed on the ec2
        * tried importing each file directly as opposed to a python package
        * looked for new installer from apt-get, yum, pip, and pip3 for various packages
        * copied and pasted directly from the github trying to fix any descrepencies
        * Felt stuck when I was able to successfully import every file correctly but the file was unable to successfully open the shared object file
        * Came to office hours 3-4:30pm 4/22/19
    * Data cap on ec2
        * removed all training pictures on ec2 instance so we could continue trying to troubleshoot the classifier.
    * Github issues
        * Github claimed info on the deployment environment was caught up to branch when it was in fact 3 commits behind
            * removed and re-cloned the repo onto the deployment environment

