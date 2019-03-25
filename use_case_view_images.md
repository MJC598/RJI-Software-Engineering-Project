## Group 4
### Use Case for Viewing All Images

### Title
View Images

#### Description
This use case is for viewing images that have already been loaded into the database system. The images will be displayed either graphically or textually. The actors involved in this process are the Photographer, Editor, and Basic User. The Photographer must take the pictures to be loaded into the database and displayed. The Editor must view the images in the database in order to categorize them. The Basic User must also be able to view the images in the database in order to determine what images are going to be selected as "good" or "bad".

#### Triggers
1. Loading of images in a database is finished, must display what has been loaded afterwards.
2. User selects option to display images.

#### Actors
* Photographer
* Basic User
* Editor

#### Preconditions
1. The database of images not being empty.

#### Main Success Scenario (Goals)
The main goal of this use case is to display the full data set of the images in the database, graphically or textually. 

#### Alternate Success Scenarios
* Not all of the images in the database are displayed.
* Images are displayed, but not in the intended way.

#### Failed End Condition
* No images are displayed in any way

#### Extensions
1. Not all of the images in the database are displayed.
    1. Notify user
    2. Prompt reload
	1. If reload fails, display only what can be loaded and inform user
    3. Display all images.
2. Images are displayed, but not properly (missing thumbnails or incomplete filenames)
    1. Prompt reload
	1. If reload fails, display what can be displayed.
    2. Display all images.

#### Steps of Execution (Requirements)
1. The user chooses to display the images in the database.
2. The database is iterated through and the images are retrieved.
3. The image files are displayed on-screen, graphically or textually.
    * If there was any error in displaying the files, a message will be shown to the user.

#### Use Case Diagram
![view images](https://github.com/MJC598/RJI-Software-Engineering-Project/blob/master/diagrams/view_images_diagram.png "view_images_diagram")

Created By: Dylan Bunch

Reviewed By: 

Collaborated With: 
