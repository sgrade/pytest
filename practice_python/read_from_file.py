# http://www.practicepython.org/exercise/2014/12/06/22-read-from-file.html

names = dict()

with open('Training_01.txt', 'r') as f:
    line = f.readline()
    while line:
        name = line.split('/')[2]
        if name not in names:
            names[name] = 1
        names[name] += 1
        line = f.readline()

print(names)
