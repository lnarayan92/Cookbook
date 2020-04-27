from urllib.parse import urlparse, urlunparse
from urllib.request import urlopen, Request

# Parse url
parsed_url = urlparse('https://www.devdungeon.com/tags/cryptography;test_params?query=test_query#test_fragment')
print(parsed_url.scheme)
print(parsed_url.netloc)
print(parsed_url.path)
print(parsed_url.params)
print(parsed_url.query)
print(parsed_url.fragment)

print('------------------------------------------')

# Construct url
url = urlunparse(('https', 'www.devdungeon.com', 'tags/cryptography', None, None, None))
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
                      'AppleWebKit/537.11 (KHTML, like Gecko) '
                      'Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'
           }
request = Request(url, None, headers)
response = urlopen(request)
print(response.read())








