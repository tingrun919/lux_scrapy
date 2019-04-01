# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JingdongItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    minPrice = scrapy.Field()
    maxPrice = scrapy.Field()
    time = scrapy.Field()
    coupon_index = scrapy.Field()
    current_url = scrapy.Field()
    pass
