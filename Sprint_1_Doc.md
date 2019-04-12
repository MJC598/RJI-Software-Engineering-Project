# Sprint 1 Design Document
#### Group 04
#### Matthew Carroll, Dylan Bunch, Olivia Bishop
---

## Deployment Environment
---
http://ec2-13-59-146-242.us-east-2.compute.amazonaws.com/

## Functional Requirements
---
1. Load Data
    A. Function 1
2. View Metadata
    A. Function 1
3. Quality Evaluation
    A. Function 1
4. View Images
    A. Function 1

## Database Design
---
#### ERD


#### DDL
We will not be using a Database because of our design structure. The pictures and classifier (which will act as a model) will sit on an external server and an API will be used to communicate all relevant data to a webpage hosted on our ec2 instance. The ranks and tags we get from the quality evaluation will be placed in the metadata of the jpg and reported to the user via the API.

## File Design
---


## Languages and Skill Gaps
---
Languages: 
1. Python
    A. Scikit Learn (Quality Evaluation)
    B. Tensorflow (Quality Evaluation)
    C. Keras (Quality Evaluation)
    D. Sewar (Quality Evaluation)
    E. Flask (API)
2. HTML
3. CSS
4. JavaScript

Skill Gaps:
1. New to most of the Python libraries
2. Not sure how we will upload photos to the server