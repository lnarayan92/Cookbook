from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
import csv


class DomainCrawler:
    # Pass self to all instance methods to refer to instance
    # Call instance methods with self
    # Constructor
    def __init__(self, base_url, filename='output.csv', max_count=25):
        self.base_url = base_url
        self.parsed_base_url = urlparse(base_url)
        self.max_count = max_count
        self.parsed_count = 0
        self.parsed_pages = []

        try:
            # csv module for csv actions - writer, writerow
            self.csv_file = csv.writer(open(filename, 'w'), delimiter=',')
        except:
            print('[-] Error loading CSV file for writing.')
        self.csv_file.writerow(['Title', 'Href'])

    def process_page(self, href):
        if self.parsed_count == self.max_count:
            return

        url = urlparse(href)
        if url.netloc == "":
            href = self.parsed_base_url.scheme + ':\\' +\
                   self.parsed_base_url.netloc +\
                   href

        # similar to include in ruby
        if href not in self.parsed_pages:
            self.parsed_pages.append(href)
        else:
            return

        print('[*] Processing %s' % href)
        self.parsed_count += 1
        try:
            response = requests.get(href)
        except:
            return

        soup = BeautifulSoup(response.text, features="html.parser")
        self.csv_file.writerow([soup.title.string, href])

        # similar to ruby each loop
        for a in soup.find_all('a'):
            if self.is_same_site_link(a.get('href')):
                self.process_page(a.get('href'))

    def is_same_site_link(self, href):
        url = urlparse(href)
        if url.netloc == '' or url.netloc == self.parsed_base_url.netloc:
            return True
        else:
            return False

    def start(self):
        self.process_page(self.base_url)
        print('[+] complete!')


if __name__ == '__main__':
    crawler = DomainCrawler('https://www.devdungeon.com/archive')
    crawler.start()
