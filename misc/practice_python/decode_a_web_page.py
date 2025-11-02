# http://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html

import requests
from bs4 import BeautifulSoup
import pprint

r = requests.get('http://www.romank.net')
# pprint.pprint(r.headers)
soup = BeautifulSoup(r.text, 'html.parser')

# print(soup.prettify())

#for link in soup.find_all('a'):
#    print(link.get('href'))

print(soup.get_text())