import json
from random import shuffle
from pathlib import Path
from os import path

num_of_items = 1000000

lst = list(range(num_of_items))
shuffle(lst)

set_of_ints = {'set_of_ints': lst}

script_dir = Path(__file__).parent.absolute()
dest_file = path.join(script_dir, 'set_of_ints.json')

with open(dest_file, 'w') as f:
    json.dump(set_of_ints, f)
