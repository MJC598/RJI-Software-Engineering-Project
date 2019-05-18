# RJI-Software-Engineering-Project
Image Quality Analysis for Mizzou Reynolds Journalism Institute
---
#### Group 4 Contributors:
1.  Matthew Carroll
2.  Olivia Bishop
3.  Dylan Bunch

#### EC2 Instance Link:
http://ec2-3-19-26-62.us-east-2.compute.amazonaws.com/index.php

#### Goal:
We hope to make a classifier for the Columbia Missouri newspaper, The Missourian, that when supplied with images, returns a quality ranking (1-10) for each of the photographs. This will reduce the number of photographs the newspaper has digitally stored and save both time and money. After trained and fully implemented, we hope to distribute it to photographers so that they can upload photos directly to the classifier and have the ranks immediately stored in our database for editor and publisher immediate use. All rights to the pictures are maintained by each of the individual photographers and are not to be distributed commerically. 

#### Dependencies:
1. [Idealo](https://github.com/idealo/image-quality-assessment)
2. TensorFlow
3. Keras

#### Environment Setup:
For specific setup instructions please go to the [developer-instructions.md](https://github.com/MJC598/RJI-Software-Engineering-Project/blob/master/developer-instructions.md) file. This gives specific instructions on setting up the entire environment. We make use of another open source ML repository called Idealo for our backend classification and then built the frontend on a standard Amazon Ubuntu EC2 Instance with Apache installed. As our project is currently fragmented we have to work in both the command line and on the website to make various changes. We used python 3.6.4 and Apache 2.0 to work on this project.

#### Current Project Status:
As of May 18, 2019, this project works in two separate parts that still need to be connected. First, the backend. This part is able to classify images on pre-trained models and print them to console. The second part is the front end. This has a website with a working navigation bar and can read from files to populate information on each of the pages. 

#### Next Steps:
Our tickets will have specifics on the next steps. A brief overview of the direction we plan to go is connecting the front and backend components. We believe this can best be done by redesigning our ML models and fixing them so that they have an output rather than a standard printout. Once this is done we can connect them to a standard webpage and retrieve values on the webpage as opposed to the console. Once here it is about cleaning up the project so it can run with a decent speed and include multiple photos at one time.   

