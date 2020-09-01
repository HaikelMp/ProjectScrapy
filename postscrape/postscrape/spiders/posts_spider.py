import scrapy

class PostsSpider(scrapy.Spider):
    name = "posts"

    start_urls = [
        'http://192.168.217.132/zipper/'
    ]

    def parse(self, response):
        page = response.url.split('/')[-1]
        filename = 'posts-%s.json' % page
        with open(filename, 'wb') as f:
            f.write(response.body)