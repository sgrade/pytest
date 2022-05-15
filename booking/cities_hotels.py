"""Booking.com interview question
http://www.glassdoor.nl/Sollicitatiegesprek/Booking-com-Sollicitatiegesprek-RVW28462301.htm
"""

# Input from STDIN

out = set()

def parse_city (string):
    """Parses city string"""
    _s = list(map(str, string.split(',')))
    # print(_s)
    _h_id, _name, _city, *_z = _s
    _h_id = _h_id.strip("{ ")
    _name = _name.strip('" ')
    _city = _city.strip('"} ')
    # print(_h_id, _name, _city)
    return _h_id, _name, _city

cities = {}

inp = input()

while True:
    inp = input()

    if inp == "]":
        break

    h_id, name, city = parse_city(inp)

    if not city in cities:
        cities[city] = {}
    if not name in cities[city]:
        cities[city][name] = set()
    cities[city][name].add(h_id)

for k, v in cities.items():
    for ho, ids in v.items():
        if len(ids) > 2:
            out.add(k)

print(list(out))
