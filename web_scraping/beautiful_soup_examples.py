from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

base_url = 'https://www.devdungeon.com/archive'
parsed_base_url = urlparse(base_url)
response = requests.get(base_url)
soup = BeautifulSoup(response.text)

for a in soup.find_all('a'):
    # print(a.get('href'))
    url = urlparse(a.get('href'))
    if url.query:
        print('query portion of the url: %s' % str(url.query))
    if url.netloc == '' or url.netloc == parsed_base_url.netloc:
        print('on-site url found: %s' % str(url))