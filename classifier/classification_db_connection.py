import os

f = []
file_list = []

for(dirpath, _, filenames) in os.walk(os.getcwd()):
    for f in filenames:
        file_list.append(os.path.abspath(os.path.join(dirpath, f)))

f = open('paths.txt', 'w')
for fl in file_list:
    f.write(fl)
    f.write('\n')
f.close()
