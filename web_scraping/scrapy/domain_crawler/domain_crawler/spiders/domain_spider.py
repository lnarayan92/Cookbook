import scrapy
import csv
from urllib.parse import urlparse


class DomainSpider(scrapy.Spider):
    name = "domain"

    def __init__(self, base_url, output_file='output_scrapy.csv', **kwargs):
        self.start_urls = [base_url]
        self.csv_file = csv.writer(open(output_file, 'w'), delimiter=',')
        self.csv_file.writerow(['Title', 'Href'])
        super().__init__(**kwargs)

    def parse(self, response):
        count = 0
        parsed_url = urlparse(response.request.url)
        for relative_url in response.css('a::attr(href)').getall():
            if count == int(self.count):
                return
            href = parsed_url.scheme + '://' + parsed_url.netloc + relative_url
            self.csv_file.writerow([href])
            count += 1
