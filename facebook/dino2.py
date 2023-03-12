# You will be supplied with two data files in CSV format. The first file contains
# statistics about various dinosaurs. The second file contains additional data.
#
# Given the following formula,
#
# speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
# Where g = 9.8 m/s^2 (gravitational constant)
#
# Write a program to read in the data files from disk, it must then print the names
# of only the bipedal dinosaurs from fastest to slowest. Do not print any other information.

# $ cat dataset1.csv
# NAME,LEG_LENGTH,DIET
# Hadrosaurus,1.2,herbivore
# Struthiomimus,0.92,omnivore
# Velociraptor,1.0,carnivore
# Triceratops,0.87,herbivore
# Euoplocephalus,1.6,herbivore
# Stegosaurus,1.40,herbivore
# Tyrannosaurus Rex,2.5,carnivore


# $ cat dataset2.csv
# NAME,STRIDE_LENGTH,STANCE
# Euoplocephalus,1.87,quadrupedal
# Stegosaurus,1.90,quadrupedal
# Tyrannosaurus Rex,5.76,bipedal
# Hadrosaurus,1.4,bipedal
# Deinonychus,1.21,bipedal
# Struthiomimus,1.34,bipedal
# Velociraptor,2.72,bipedal

from math import sqrt

g = 9.8

stride_lengths = {}
with open('facebook/dataset2.csv') as ds2:
    ds2.readline()
    for line in ds2:
        ls = line.split(',')
        stance = ls[2].rstrip()
        if stance != 'bipedal':
            continue
        name = ls[0]
        leg_len = float(ls[1])
        stride_lengths[name] = leg_len

leg_lengths = {}
with open('facebook/dataset1.csv') as ds1:
    ds1.readline()
    for line in ds1:
        name, leg_len, _ = line.split(',')
        if name not in stride_lengths.keys():
            continue
        leg_lengths[name] = float(leg_len)

def get_speed(name):
    return ((stride_lengths[name] / leg_lengths[name]) - 1) * (sqrt(leg_lengths[name]) * g)

x = get_speed('Velociraptor')

name_and_speed = [(name, get_speed(name)) for name in leg_lengths.keys()]
pre_ans = sorted(name_and_speed, key = lambda x: x[1], reverse=True)
ans = ('\n').join([element[0] for element in pre_ans])

print(ans)
