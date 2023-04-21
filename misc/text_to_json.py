# import requests
# import mysql.connector
# import pandas as pd

from datetime import datetime
import json

"""
Example input (entire string):

123 Gamble Street, Dallas, TX 75083
45 Oscar Tries Ave, Apt 404, Issaquah, WA 59433
9001 Edith Boulevard #101, New York City, NY 98101

/opt/addresses/<millisecond timestamp>.json
[
    {
        "street_number": 123,
        "street": "Gamble Street",
        "city": "Dallas",
        "state": "TX",
        "zip": 75083,
    },
    {
        
    }
]   

"""

def save_addresses(addresses_str: str):
    """
    Save structured addresses to "/opt/addresses/<millisecond timestamp>.json"
    """

    try:    
        output = [] # list of dicts
        
        input_list = addresses_str.split(sep='\n') # list of lines
        
        for line in input_list:
            
            line_splitted = line.split(sep=', ')    # ["123 Gamble Street", "Dallas", "TX 75083"]
            
            first_space_idx = line_splitted[0].find(' ')
            street_number = line_splitted[0][:first_space_idx]
            street_name = line_splitted[0][first_space_idx + 1:]
            
            ext = line_splitted[1] if len(line_splitted) == 4 else ""

            city = line_splitted[-2]

            state, postcode = line_splitted[-1].split()

            line_dict = {}
            line_dict["street_number"] = street_number
            line_dict["street_name"] = street_name
            line_dict["ext"] = ext
            line_dict["city"] = city
            line_dict["state"] = state
            line_dict["zip"] = postcode

            output.append(line_dict)
        
        output_json = json.dumps(output)
        print(output_json)

        dt = datetime.now()
        # getting the timestamp
        ts = datetime.timestamp(dt)
        
        dest_filename = str(ts) + ".json"
        print(dest_filename)
        
        with open (dest_filename, 'w') as f:
            json.dump(output_json, f)

    except:
        print("will process exceptions later")


inp = """123 Gamble Street, Dallas, TX 75083
45 Oscar Tries Ave, Apt 404, Issaquah, WA 59433
9001 Edith Boulevard #101, New York City, NY 98101"""

save_addresses(inp)
