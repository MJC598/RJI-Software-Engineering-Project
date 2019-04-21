"""import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config['DEBUG'] = True

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route('/', methods=['GET'])
def start():
    return "<h1>Testing</h1>"

@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)


app.run()"""

"""def get_sample_images_json():
    json_string1 = get_images_from_url('http://rji.augurlabs.io/20170902_MuMsu/1q/')
    json_string1 = json_string1[:-1] + ','
    json_string2 = get_images_from_url('http://rji.augurlabs.io/20170902_MuMsu/2q/')
    json_string2 = " " + json_string2[1:]
    json_string2 = json_string2[:-1] + ','
    json_string3 = get_images_from_url('http://rji.augurlabs.io/20170902_MuMsu/3q/')
    json_string3 = " " + json_string3[1:]
    json_string3 = json_string3[:-1] + ','
    json_string4 = get_images_from_url('http://rji.augurlabs.io/20170902_MuMsu/4q/')
    json_string4 = " " + json_string4[1:]
    json_string4 = json_string4[:-1] + ',' 
    json_string5 = get_images_from_url('http://rji.augurlabs.io/20170909_MuSc/1q/')
    json_string5 = " " + json_string5[1:]
    json_string5 = json_string5[:-1] + ',' 
    json_string6 = get_images_from_url('http://rji.augurlabs.io/20170909_MuSc/2q/')
    json_string6 = " " + json_string6[1:]
    json_string6 = json_string6[:-1] + ','
    json_string7 = get_images_from_url('http://rji.augurlabs.io/20170909_MuSc/3q/')
    json_string7 = " " + json_string7[1:]
    json_string7 = json_string7[:-1] + ',' 
    json_string8 = get_images_from_url('http://rji.augurlabs.io/20170909_MuSc/4q/')
    json_string8 = " " + json_string8[1:]
    json_string = json_string1 + json_string2 + json_string3 + json_string4 + json_string5 + json_string6 + json_string6 + json_string7 + json_string8
    with open('data.json', 'w') as outfile:
        json.dump(json_string,outfile)


get_sample_images_json()"""


import requests, re, json

# creates a json string of tuples in the form [('filename', 'full_url_of_image')]
def get_images_from_url_obj(url):
    
    # get the directory, its output is basically an HTML document with anchor tags for each image
    r = requests.get(url)

    # parses the HTML document and grabs everything inside quotation marks and stores these filenames in list a
    a = re.findall('"([^"]*)"', r.text)

    # add the url to each filename and store this full path in list b
    url += '{0}'
    b = [url.format(i) for i in a]

    # zip the two lists together and ditch the first element since it's invariably '../'; store in list c
    c = list(zip(a,b))
    c.pop(0)

    # return the object, not a json string
    return c


def get_images_from_url_json(url):

    # get the directory, its output is basically an HTML document with anchor tags for each image
    r = requests.get(url)

    # parses the HTML document and grabs everything inside quotation marks and stores these filenames in list a
    a = re.findall('"([^"]*)"', r.text)

    # add the url to each filename and store this full path in list b
    url += '{0}'
    b = [url.format(i) for i in a]

    # zip the two lists together and ditch the first element since it's invariably '../'; store in list c
    c = list(zip(a,b))
    c.pop(0)

    # turn c into a json_string
    json_string = json.dumps(c)

    # this is for testing. I do not recommend uncommenting this line, it is a very large output.
    # print json_string

    # return json string, not an object
    return json_string


def format_names_and_ratings(names, ratings):

    # the big list
    names_and_ratings = []

    # loop through the names one at a time
    for i in range(0,len(names)):
        
        # create a new list to store into the big list
        adding_list = [names[i][0], str(ratings[2 * i]), str(ratings[(2 * i) + 1])]

        # append the new list to the list of lists
        names_and_ratings.append(adding_list)

    json_names_and_ratings = json.dumps(names_and_ratings)

    # return the newly created names and ratings; looks like [['name1', 'r1', 'r2'], [...], ['nameN', 'r2N-1', 'r2N']]
    # return names_and_ratings 

    return json_names_and_ratings


if __name__ == '__main__':

    # some test variables to ensure that things are working properly

    #gets around 1000 images in ["filename", "filepath"] format
    test_names = get_images_from_url_obj('http://rji.augurlabs.io/20170902_MuMsu/1q/')

    # creates a list of length equal to 2 times the number of elements in test_names to simulate the ratings for the images
    test_ratings = []
    for x in range(0,2 * len(test_names)):
        test_ratings.append(x)

    # combine the names of the images with the 2 ratings for said image into one big list
    test_names_and_ratings = format_names_and_ratings(test_names,test_ratings)

    # this is just for testing
    print test_names_and_ratings
