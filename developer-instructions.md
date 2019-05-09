# Developer Instructions

## Setup
1. Fork idealo repository from https://github.com/idealo/image-quality-assessment to start setting up backend

2. Stand up ubuntu Amazon EC2 instance and ssh into the terminal

3. Download and install updates for EC2 and Apache
    * We did this because we know Apache best, it should work with any preferred way to stand up a backend for a website
    * We also put both repositories inside the /var/www/ directory for ease of communication
        * This required we chmod to change the respective permissions on the directory for acccess between our repository and idealo

4. Once the idealo repository has been cloned and added to the EC2 instance follow the README.md instructions on their repository. If you have images and labels feel free to retrain the models, otherwise we just use a bash script to run the models as they were presented.

5. Clone our repository next to the idealo repository and navigate to the classifier folder.

6. Inside you should find a shell script that can be run to get results out of the idealo machine learning model, adjust the script with the location of your images and move the shell script to the idealo repo. Every execution should give you results printed to standard out now.


## Execution
1. Visit http://ec2-3-19-26-62.us-east-2.compute.amazonaws.com

2. To **search** a specific image, ranking, resolution or type (sports, etc) select the search tab and enter criteria in the search bar.

3. To **upload** images or folders of images, navigate to the upload tab, choose a file(s) to upload, and click upload button.

4. To **view** images that have been uploaded, ran through the classifier, and ranked, click the view images tab. 
