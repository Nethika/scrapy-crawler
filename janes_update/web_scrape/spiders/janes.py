import scrapy
from scrapy.loader.processors import Join


class ArchiveSpider(scrapy.Spider):
    name = 'janes'

    start_urls = ['http://www.janes.com/archive']

    def parse(self, response):
        # follow links to article pages
        for href in response.css('#search-results a::attr(href)').extract():
            yield scrapy.Request(response.urljoin(href),
                                 callback=self.parse_article)

        # follow pagination links
        next_page = response.css('.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_article(self, response):
        def extract_with_css1(query):
            texts = Join()
            desc = response.css(query).extract()
            desc = [s.strip() for s in desc]
            texts_all = texts(desc)
            return texts_all
        def extract_with_css2(query):
            return response.css(query).extract_first().strip()      
        def extract_with_css3(query):
            texts = Join()
            desc = response.css(query).re(r'IHS.*')
            desc = [s.strip() for s in desc]
            texts_all = texts(desc)
            return texts_all

        yield {
            'title': extract_with_css2('h1::text'),
            'link':response.request.url,
            'date': extract_with_css2('.date::text'),
            'author': extract_with_css1('.byline b::text'),
            'IHS':extract_with_css3('.byline::text'),            
            'text': extract_with_css1('p::text'),
            'key_points': extract_with_css1('#article li::text'),
            'category':extract_with_css2('div.section-title::text'),
        }
