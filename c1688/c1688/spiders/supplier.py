# -*- coding: utf-8 -*-
import re
import urllib
import sys
import scrapy

class SupplierSpider(scrapy.Spider):
    heart_beat = 0
    name = "supplier"
    allowed_domains = ["1688.com", "alicdn.com"]
    laputa_url = 'https://laputa.1688.com/offer/ajax/widgetList.do?data=offerdetail_ditto_title%2Cofferdetail_common_report%2Cofferdetail_ditto_serviceDesc%2Cofferdetail_ditto_preferential%2Cofferdetail_ditto_postage%2Cofferdetail_ditto_offerSatisfaction%2Cofferdetail_w1190_tradeWay%2Cofferdetail_ditto_samplePromotion&offerId='
    compare_keys = [
        u'哎呀呀',
        u'名创优品',
        u'miniso',
        u'严选',
        u'yanxuan',
        u'丽芙',
        u'lifevc'
        u'无印良品',
        u'無印良品',
        u'muji',
        u'诸城鲁源纺织'
    ]

    def start_requests(self):
        search_key = self.settings['SEARCH_KEY']
        compare_keys = SupplierSpider.compare_keys
        print "======", "search_key:", search_key, '======'
        print "======", "compare_keys:", SupplierSpider.compare_keys, '======'
        if search_key and compare_keys:
            start_url = 'https://www.1688.com/gongsi/-.html?keywords=' + \
                urllib.quote(search_key.decode(
                    sys.stdin.encoding or 'utf8').encode('gbk'))
            print "======", "start_url:", start_url, '======'
            yield scrapy.Request(url=start_url, callback=self.parse)

    def parse(self, response):
        hit = self.check_hit(response, response.request.url)
        if hit:
            yield hit
        for product_url in response.xpath('//ul[@class=\"qg-offerresults offers"]/li[@class=\"fd-clr\"]//a[@class=\"boxImg\"]/@href').extract():
            if product_url:
                yield scrapy.Request(product_url, callback=self.parse_product)
        next_page = response.xpath(
            '//a[@class=\"page-next\"]/@href').extract_first()
        if next_page:
            print '======', next_page, '======'
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_product(self, response):
        hit = self.check_hit(response, response.request.url)
        if hit:
            yield hit
        else:
            tfs_url = response.xpath(
                '//div[@id=\"desc-lazyload-container\"]/@data-tfs-url').extract_first()
            if tfs_url:
                yield scrapy.Request(tfs_url, callback=self.parse_tfs, meta={'url': response.request.url})

    def parse_tfs(self, response):
        hit = self.check_hit(response, response.meta['url'])
        if hit:
            yield hit

    def check_hit(self, response, url):
        body = response.xpath('//*').extract_first()
        hit = False
        for compare_key in SupplierSpider.compare_keys:
            if re.search(compare_key, body, re.IGNORECASE):
                hit = True
                # print(" hit =========== %s, url: %s", compare_key, response.meta['url'])
                return {
                    'search_key': self.settings['SEARCH_KEY'],
                    'hit_key': compare_key,
                    'url': url
                }
