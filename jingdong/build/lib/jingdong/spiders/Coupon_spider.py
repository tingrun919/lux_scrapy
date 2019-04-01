# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider, Request, FormRequest
from jingdong.items import JingdongItem


class Coupon(scrapy.Spider):
    name = "coupon"
    allowed_domains = ["jd.com"]
    start_url = 'https://a.jd.com/coupons.html'

    def __init__(self, keyword='酒店', keyword2='500', *args, **kwargs):
        super(Coupon, self).__init__(*args, **kwargs)
        self.keyword = keyword
        self.keyword2 = keyword2

    def start_requests(self):
       return [Request(self.start_url, callback=self.coupon_detail)]

    def coupon_detail(self, response):
        next_page = response.xpath('/html/body/div[5]/div/div[2]/div[2]/div/div[2]/div/a[9]//@href').extract()
        for sel in response.xpath('//*[@id="coupons-list"]'):
            name = sel.xpath('//div[1]/div[2]/div[1]/p//@title').extract()
            item = JingdongItem()
            item['name'] = name
            yield item