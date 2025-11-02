# http://www.practicepython.org/exercise/2014/11/30/21-write-to-a-file.html

import requests
from bs4 import BeautifulSoup
import pprint


r = requests.get('http://www.romank.net')
# pprint.pprint(r.headers)
soup = BeautifulSoup(r.text, 'html.parser')

# print(soup.prettify())

#for link in soup.find_all('a'):
#    print(link.get('href'))

#print(soup.get_text())

with open('file_to_save.txt', 'w') as open_file:
    open_file.write(soup.prettify())
