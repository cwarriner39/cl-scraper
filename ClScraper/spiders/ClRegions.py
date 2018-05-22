# -*- coding: utf-8 -*-
import scrapy


class ClregionsSpider(scrapy.Spider):
    name = 'ClRegions'
    allowed_domains = ['www.craigslist.org']
    start_urls = ['https://www.craigslist.org/about/sites/']
    custom_settings = {
        'CONCURRENT_REQUESTS': 1,
        'DOWNLOAD_DELAY': 1,
    }

    def parse(self, response):
        yield {'region': response.css('div.box_1 h4::text').extract(),}
        for localGroup in response.css('div.box_1 ul'):
            yield {'cities': localGroup.css('li a::text').extract() }

        yield {'region': response.css('div.box_2 h4::text').extract(),}
        for localGroup in response.css('div.box_2 ul'):
            yield {'cities': localGroup.css('li a::text').extract() }

        yield {'region': response.css('div.box_3 h4::text').extract(),}
        for localGroup in response.css('div.box_3 ul'):
            yield {'cities': localGroup.css('li a::text').extract() }

        yield {'region': response.css('div.box_4 h4::text').extract(),}
        for localGroup in response.css('div.box_4 ul'):
            yield {'cities': localGroup.css('li a::text').extract() }
