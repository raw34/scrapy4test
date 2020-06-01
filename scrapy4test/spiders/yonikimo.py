# -*- coding: utf-8 -*-
import scrapy


class YonikimoSpider(scrapy.Spider):
    name = 'yonikimo'
    allowed_domains = ['yonikimo.com']
    start_urls = ['http://yonikimo.com/story.html']

    def parse(self, response):
        for story in response.xpath('//*[@id="top"]').xpath('//table/tr'):
            yield{
                '//*[@id="top"]/table/tbody/tr[5]/td[2]/a'
                'no': story.xpath('td[1]/text()').extract(),
                'title': story.xpath('td[2]/a/text()').extract(),  
                'url': story.xpath('td[2]/a/@href').extract(),  
                'cast': story.xpath('td[3]/text()').extract(),
                'comment': story.xpath('td[4]/text()').extract(),
            }
            pass
        pass
