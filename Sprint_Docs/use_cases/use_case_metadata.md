#### Group 4
#### Use Case for Viewing Metadata

### Title
View Metadata

#### Description
This use case is specifically for a user looking at the tags and metadata applied to a specific image by the classifier. Data presented will include reference tags, size, and image quality rank. The actors involved in viewing the metadata are editors and basic users. The editor must select the specific image from the view images system to enter this described subsystem. Then they can view all components and metadata about the inteded image. 

#### Triggers
1. The user selecting a specific image from the dataset. 

#### Actors
* Editor
* Basic User

#### Preconditions
1. A photo must have metadata to be presented to the editor.
2. Photos must have unique identifying IDs.

#### Main Success Scenario (Goals)
The main success scenario of this system is a user or editor being able to see the correct metadata information associated with the picture including the overall assigned quality ranking.

#### Alternate Success Scenarios
* No metadata is present.
* Only some of the metadata fields are populated.

#### Failed End Condition
* Incorrect metadata is displayed.
* The system fails to notify the user if there are problems.

#### Extensions
1. No metadata is present.
    1. Inform user of the lack of metadata.
        1. If the user is an editor give option to run photo through quality tester to populate metadata.
        2. If user is basic user present them with a way to return to the viewing images system.
    2. Continue through with user choices.
2. Only some of the metadata fields are populated.
    1. Inform user of the error.
    2. Log error report.
    3. Prompt user to return to other images.

#### Steps of Execution (Requirements)
1. The user is prompted to select a folder of images or an individual image.
2. The program will recursively go through the folder(s) and open each image.
    * The images will be either pre-defined as "good" or as "bad",  or the current image loaded will be presented to the user (Editor) to choose whether the image is "good" or "bad".
3. The image path and rating will be stored in some fashion (textually, etc.) for later retrieval.
4. The data has finished loading into the system and is ready to classify a new data set.

#### Use Case Diagram
![load data](https://github.com/MJC598/RJI-Software-Engineering-Project/blob/master/diagrams/view_metadata.png "view_metadata_diagram")

Created By: Matthew Carroll

Reviewed By: Olivia Bishop

Collaborated With:
