# -*- coding: utf-8 -*-
import scrapy
from fancy.items import FancyItem
from scrapy import Request
from scrapy.selector import Selector

class Fancy(scrapy.Spider):
    name = "fancy"
    allowed_domains = ["fancy.com"]
    start_urls = [
        'https://m.fancy.com/'
    ]

    def parse(self, response):
		base_url="https://m.fancy.com"
		response_selector = Selector(response)
		for sel,price,follow,image_url,link in zip(response.xpath('//figcaption/a/text()').extract(),
								response.xpath('//figcaption/span/a[2]/text()').extract(),
								response.xpath('//figcaption/span/a[1]/text()').extract(),
								response.xpath('//figure/span/video[@poster]//@poster | //*[@id="thing-img-"]//@src').extract(),
								response.xpath('//figcaption/a//@href').extract()):
			if 'https://' in image_url:
				yield FancyItem(name = sel,price = price,follow = follow,image = image_url,link = 'https://m.fancy.com'+link)
			else:
				yield FancyItem(name = sel,price = price,follow = follow,image = 'https:'+image_url,link = 'https://m.fancy.com'+link)

		urls = base_url+str(response_selector.xpath('//*[@id="pagination_div"]/a[2]/@href').extract_first())
		for url in urls:
			yield scrapy.Request(urls, callback=self.parse)