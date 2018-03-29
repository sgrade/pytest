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


import math


class CheckDinosaurs:

    def __init__(self, file1, file2):
        """ think later

        self._file1_as_a_string =
        self._file1_as_a_string =
         """

        self._f1 = file1
        self._f2 = file2

        self._list_of_names_with_bipedal = list()

        self._dict_with_parameters_for_speed_calculations = {
            name: [0, 0] for name in self._list_of_names_with_bipedal
        }

        self._bipedal_dict_with_speed = dict()

    def _get_bipedal(self):
        """return the list of bipedal ones from the second file"""
        # bipedal_list = list()
        with open('dataset2.csv') as f2:
            f2_as_a_list_of_lines = f2.readlines()
            for dino in f2_as_a_list_of_lines:
                # \n
                if dino.split(',')[-1].strip() == 'bipedal':
                    self._list_of_names_with_bipedal.append(dino)
        return self._list_of_names_with_bipedal

    def _get_data_for_speed_calculations(self):
        """

        :return:
        get bipedal list and do some list comprehensions to get speed
        :return: dict: name:speed
        a = dict{
            name: [leg_length, stride_length]
        }
        """

        with open(self._f1) as f1:
            """Docstring later"""
            # Processing f1:
            f1_as_a_list_of_lines = f1.readlines()
            for element in self._list_of_names_with_bipedal:
                name = element.split(',')[0]
                for row in f1_as_a_list_of_lines:
                    if row.startswith(name):
                        leg_length = float(row.split(',')[1])
                        self._dict_with_parameters_for_speed_calculations[name] = [leg_length, 0]

        with open(self._f2) as f2:
            """Docstring later"""
            f2_as_a_list_of_lines = f2.readlines()
            for element in self._list_of_names_with_bipedal:
                name = element.split(',')[0]
                try:
                    for row in f2_as_a_list_of_lines:
                        if row.startswith(name):
                            stride_length = float(row.split(',')[1])
                            self._dict_with_parameters_for_speed_calculations[name][-1] = stride_length
                except KeyError:
                    # print('there is not enough information to calculate speed for', name)
                    pass

        return self._dict_with_parameters_for_speed_calculations

    def _calculate_speed(self):
        # calculating speed
        g = 9.8
        for dino, parameters in self._dict_with_parameters_for_speed_calculations.items():
            stride_len = parameters[-1]
            leg_len = parameters[0]
            # speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
            speed = ((stride_len / leg_len) - 1) * math.sqrt(leg_len * g)
            self._bipedal_dict_with_speed[speed] = dino

        return self._bipedal_dict_with_speed

    def sort_by_speed(self):

        self._get_bipedal()

        self._get_data_for_speed_calculations()

        self._calculate_speed()

        # sort from fastest to slowest
        x = reversed(sorted(self._bipedal_dict_with_speed.items()))
        for item in x:
            print(item[1])


x = CheckDinosaurs('dataset1.csv', 'dataset2.csv')
x.sort_by_speed()
