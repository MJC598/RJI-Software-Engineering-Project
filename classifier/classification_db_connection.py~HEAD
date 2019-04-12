import os

f = []
file_list = []

for(dirpath, _, filenames) in os.walk(mypath):
    for f in filenames:
        file_list.append(os.path.abspath(os.path.join(dirpath, f)))

f = open('paths.txt', 'w')
f.write(file_list)
f.close()