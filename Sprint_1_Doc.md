# Sprint 1 Design Document
#### Group 04
#### Matthew Carroll, Dylan Bunch, Olivia Bishop


## Deployment Environment

http://ec2-13-59-146-242.us-east-2.compute.amazonaws.com/

## Functional Requirements

1. Load Data
    * load\_data()
	* Runs on RJI server
	* Retrieves file paths and metadata regarding classification from RJI server calling get\_file\_paths(), get\_scores(), and get\_metadata()
	* Sends the data back to our server and props up a flask database to hold image paths and scores for easy retrieval/display
2. View Metadata
    * view\_metadata()
	* Reads metadata from flask database from retrieve\_metadata(picture)
	* Calls function in the view to display images with corresponding metadata in a readable fashion via display\_metadata(picture)
	* Optionally displays corresponding image with display\_image(picture)
3. Quality Evaluation
    * evaluate\_quality()
	* Runs on RJI server
	* File paths to evaluate sent from our flask database to RJI server via evaluate\_these\_files(files[]) and calls classify() for each
	* Writes quality score to metadata via store\_score(picture,score)
	* If files are updated, send new score data back to flask database with update\_quality\_score(picture,score)
4. View Images
    * view\_images()
	* Select number of images viewed in paginated form via retrieve\_images(files[]), say 200 at a time, stores on server and deletes upon moving to new page
	* Call ui function to display them on page (with/without corresponding score) via display\_images() (reading images from temporary directory)

## Database Design

#### ERD


#### DDL
We will not be using a Database because of our design structure. The pictures and classifier (which will act as a model) will sit on an external server and an API will be used to communicate all relevant data to a webpage hosted on our ec2 instance. The ranks and tags we get from the quality evaluation will be placed in the metadata of the jpg and reported to the user via the API.

## File Design

1. /ui/
    * index.html
	* View Images, View Metadata
	* This is the primary file for the website's design, styling, and functionality
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

## Languages and Skill Gaps

Languages: 
1. Python
    * Scikit Learn (Quality Evaluation)
    * Tensorflow (Quality Evaluation)
    * Keras (Quality Evaluation)
    * Sewar (Quality Evaluation)
    * Flask (API)
2. HTML
    * Markup language for ui
3. CSS
    * Styling for HTML
4. JavaScript
    * Make the webpage dynamic

Skill Gaps:
1. New to most of the Python libraries
2. Not sure how we will upload photos to the server
