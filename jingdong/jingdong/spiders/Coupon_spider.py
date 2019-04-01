# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider, Request, FormRequest
from jingdong.items import JingdongItem
import sys,urllib 


class Coupon(scrapy.Spider):
    name = "coupon"
    allowed_domains = ["jd.com"]
    start_url = 'https://a.jd.com/coupons.html'

    def __init__(self, keyword='图书', keyword2='200', *args, **kwargs):
        super(Coupon, self).__init__(*args, **kwargs)
        self.keyword = keyword
        self.keyword2 = keyword2
        #self.keyword = urllib.quote(keyword.decode(sys.stdin.encoding).encode('gbk')) #第一个关键字
        #self.keyword2 = urllib.quote(keyword2.decode(sys.stdin.encoding).encode('gbk')) #第二个关键字

    def start_requests(self):
       yield scrapy.Request(self.start_url, callback=self.coupon_detail)

    def coupon_detail(self, response):
        url = 'https://a.jd.com/batchTime.html'
        for time in response.xpath('//div[1]/div[2]/div[3]//@coupon-time').extract():
            yield FormRequest(url, formdata={'batchId':time}, callback=self.get_time)

    def get_time(self, response):
        


