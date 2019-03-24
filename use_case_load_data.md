## Group 4
### Use Case for Loading Data

### Title
Load Data

#### Description
This use case is specifically for loading the data into the system in order to begin processing the data. Involved in this process is the Photographer as they must take the pictures that are to be entered into the system. The Editor's job is to train the neural network on the data set of images provided by the Photographer. The Basic User in this use case uses the software, trained by the Editor, on the data set, provided by the Photographer.

#### Triggers
1. The user entering in a new data set to be processed.
2. The dataset being empty, so the user is prompted to enter in a data set. 

#### Actors
* Photographer
* Editor
* Basic User

#### Preconditions
1. There must be a data set to be loaded.
2. There must be an Editor distinguished.

#### Main Success Scenario (Goals)
For this use case to succeed, the whole data set must be loaded into the database.

#### Alternate Success Scenarios
* Data set is partially loaded, due to some corrupt files or unsupported file types.
* Data set is fully loaded, but some files were not stored in the database.

#### Failed End Condition
The data set is not loaded and, thus, no displayed information is present.

#### Extensions


#### Steps of Execution (Requirements)
1. The user is prompted to select a folder of images or an individual image.
2. The program will recursively go through the folder(s) and open each image.
    * The images will be either pre-defined as "good" or as "bad",  or the current image loaded will be presented to the user (Editor) to choose whether the image is "good" or "bad".
3. The image path and rating will be stored in some fashion (textually, etc.) for later retrieval.
4. The data has finished loading into the system and is ready to classify a new data set.

#### Use Case Diagram


Created By: Dylan Bunch

Reviewed By:

Collaborated With:
