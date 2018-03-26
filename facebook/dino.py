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


class CheckDinosaurs:

    def __init__(self, file1, file2):
        """ think later

        self._file1_as_a_string =
        self._file1_as_a_string =
         """

        self._list_of_names_with_bipedal = list()

        pass

    get_bipedal(self):
    """return the list of bipedal ones from the second file"""
    bipedal_list = list()
    with open('dataset2.csv') as f2:
        f2_as_a_list_of_lines = f2.readlines()
        for dino in f2_as_a_list_of_lines:
            # \n
            if dino.split(',')[-1].strip() == 'bipedal'
                bipedal_list.append(dino)
    return bipedal_list


calculate_speed(self):
"""get bipedal list and do some list comprehensions to get speed
return: dict: name:speed
"""
"""
a = dict{
    name: [leg_length, stride_length]
}

"""
dict_with_parameters_for_speed_calculations = {name: [0, 0] for name in self._list_of_names_with_bipedal}

with open('dataset1.csv') as f1:
    """Docstring later"""

    # Processing f1:
    f1_as_a_list_of_lines = f1.readlines()
    for name in self._list_of_names_with_bipedal:
        for row in f1_as_a_list_of_lines:
            if row.startswith(name):
                leg_length = float(row.split(',')[1])
                dict_with_parameters_for_speed_calculations[name] = [leg_length, 0]

    # Processing f2:
    f2_as_a_list_of_lines = f2.readlines()
    for name in self._list_of_names_with_bipedal:
        for row in f2_as_a_list_of_lines:
            if row.startswith(name):
                stride_length = float(row.split(',')[1])
                dict_with_parameters_for_speed_calculations[name][-1] = stride_lenght

    # calculating speed

    # speed formula
    speed =

    # speed = 0
return bipedal_list_with_speed

sort_by_speed(self):
"""retrurn sorted list"""
# Check if below requires any input parameter
# get our bi_list
bi_list = self.get_bipedal()

# get names from bi_list
for element in bi_list:
    self._list_of_names_with_bipedal.append(element.split(',')[0])

# for each name calculate speed


# for each name add speed to bi_list

# sort it
return sorted_by_speed

x = CheckDinosaurs()
print(x.sort_by_speed())
