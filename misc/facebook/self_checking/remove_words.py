import re

cleaned_lines = list()

"""
# Using lists
def remove_words(file, words):
    with open(file, 'r+') as f:
        # parse line by line
        for line in f:
            x = line.strip().split(' ')
            #
            cleaned_line = [word for word in x if word not in words]
            #
            cleaned_lines.append(cleaned_line)

        # converting back to a string from lists
        list_of_joined_strings = [' '.join(element) for element in cleaned_lines]
        output = ' \n'.join(list_of_joined_strings) + '\n'

        f.seek(0)
        f.write(output)
        f.truncate()
"""


# Same, but using regular expressions
def remove_words(file, words):
    patterns = [r'\b' + word + r'\b' for word in words]
    patterns = [re.compile(element) for element in patterns]
    with open(file, 'r+') as f:
        string_to_process = f.read()
        for p in patterns:
            string_to_process = p.sub('', string_to_process)
        f.seek(0)
        f.write(string_to_process)
        f.truncate()


filename = 'remove_words.txt'
words_to_remove = ['word', 'to', 'remove']
remove_words(filename, words_to_remove)
