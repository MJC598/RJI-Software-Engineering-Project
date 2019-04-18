"""import urllib2

url2 = "http://rji.augurlabs.io/20170902_MuMsu/4q/20170921_mumsu_jd_"
url1 = "http://rji.augurlabs.io/20170902_MuMsu/4q/20170921_mumsu_mp_"
exten = ".JPG"

def download_web_image(url, x):
    request = urllib2.Request(url)
    img = urllib2.urlopen(request).read()
    with open ("pictures/" + str(x) + ".jpg", 'w') as f: f.write(img)

for x in range(4384,4741):
    # download_web_image("http://upload.wikimedia.org/wikipedia/commons/8/8c/JPEG_example_JPG_RIP_025.jpg")
    download_web_image(url1 + str(x) + exten, x) 
"""
"""import os
import urllib2

url = "http://rji.augurlabs.io/20170902_MuMsu/1q/"
imgdir = urllib2.urlopen(url).read()
for file in os.listdir(imgdir):
    if file.endswith(".JPG"):
        print(os.path.join(url,file) + "\n")
"""

import requests
import re
url = 'http://rji.augurlabs.io/20170902_MuMsu/1q/'
r = requests.get(url)
# print r.text
a = re.findall('"([^"]*)"', r.text)
for x in range(len(a)):
    if x > 0:
        print url + a[x]
