# -*- coding: utf-8 -*-
import scrapy
# from scrapy.linkextractors import LinkExtractor
from ..items import MatpItem

class MatplotSpider(scrapy.Spider):
    name = "matplot"
    allowed_domains = ["matplotlib.org"]
    start_urls = ['https://matplotlib.org/gallery.html']

    def parse(self, response):
        figs = response.xpath('//*[@id="statistics"]/figure/figcaption')

        for fig in figs:
            url = 'https://matplotlib.org/' + fig.xpath('a/@href').extract_first()

            yield scrapy.Request(url, callback = self.parse_link)


    def parse_link(self, response):
        href = response.css('a.reference.external::attr(href)').extract_first()
        url = response.urljoin(href)
        matpl = MatpItem()
        matpl['file_urls'] = [url]

        return matpl
