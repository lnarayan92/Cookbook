import scrapy
import csv
# from urllib.parse import urlparse


class DomainSpider(scrapy.Spider):
    name = "domain"

    def __init__(self, base_url, output_file='output_scrapy.csv', **kwargs):
        self.start_urls = [base_url]
        self.csv_file = csv.writer(open(output_file, 'w'), delimiter=',')
        self.csv_file.writerow(['Title', 'Href'])
        self.parsed_url_count = 0
        super().__init__(**kwargs)
        print('countt' + str(int(self.max_count)))

    def parse(self, response):
        # count = 0
        # parsed_url = urlparse(response.request.url)
        # for relative_url in response.css('a::attr(href)').getall():
        #     if count == int(self.max_count):
        #         return
        #     href = parsed_url.scheme + '://' + parsed_url.netloc + relative_url
        #     self.csv_file.writerow([response.css('title::text'), href])
        #     count += 1
        if self.parsed_url_count > int(self.max_count):
            return
        else:
            print('[*] Parsed url count is %s' % str(self.parsed_url_count))
            print('[*] Parsed url is %s' % str(response.url))
            self.parsed_url_count += 1
            self.csv_file.writerow([response.css('title::text').get(), response.url])
            for a in response.css('a'):
                try:
                    yield response.follow(a, callback=self.parse)
                except:
                    return