# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider,Request,FormRequest
import sys,urllib 
from supplier.items import SupplierItem
import time
import re

class Supplier(scrapy.Spider):
    name = 'supplier'
    allowed_domains = ['1688.com']
    start_url = ['https://vip.1688.com/mc/buyer_index.htm']

    def __init__(self, keyword="济南", keyword2="卫生纸", *args, **kwargs):
        super(Supplier, self).__init__(*args, **kwargs)
        self.keyword = urllib.quote(keyword.decode(sys.stdin.encoding).encode('gbk')) #第一个关键字
        self.keyword2 = urllib.quote(keyword2.decode(sys.stdin.encoding).encode('gbk')) #第二个关键字
        #print 11111
        #s = ['\r\n    \t\t\t\t\t\t\t\xe3\x80\x80   \xe5\xb1\xb1\xe4\xb8\x9c\xe6\xa2\x85\xe7\xac\x9b\xe5\x8c\xbb\xe7\x96\x97\xe7\x94\xa8\xe5\x93\x81\xe6\x9c\x89\xe9\x99\x90\xe5\x85\xac\xe5\x8f\xb8\xe5\x88\x9b\xe5\xbb\xba\xe4\xba\x8e2000\xe5\xb9\xb4\xe3\x80\x82\xe5\x8d\x81\xe4\xba\x94\xe5\xb9\xb4\xe6\x9d\xa5\xef\xbc\x8c\xe6\xa2\x85\xe7\xac\x9b\xe5\x9d\x9a\xe6\x8c\x81\xe3\x80\x8c\xe5\x8b\x87\xe4\xba\x8e\xe5\xbc\x80\xe6\x8b\x93\xef\xbc\x8c\xe4\xb8\x8d\xe6\x96\xad\xe5\x88\x9b\xe6\x96\xb0\xe3\x80\x8d \xe7\x9a\x84\xe6\x96\xb9\xe9\x92\x88\xef\xbc\x8c\xe4\xb8\x93\xe6\xb3\xa8\xe7\xa0\x94\xe4\xba\xa7\xe9\xab\x98\xe7\xba\xa7\xe7\x94\x9f\xe6\xb4\xbb\xe7\x94\xa8\xe7\xba\xb8\xe5\x92\x8c\xe6\xaf\x8d\xe5\xa9\xb4\xe7\x94\xa8\xe5\x93\x81\xe3\x80\x82\xe6\x97\xb6\xe8\x87\xb3\xe4\xbb\x8a\xe5\xa4\xa9\xef\xbc\x8c\xe6\xa2\x85\xe7\xac\x9b\xe5\xb7\xb2\xe9\x80\x90\xe6\xb8\x90\xe6\x88\x90\xe9\x95\xbf\xe4\xb8\xba\xe4\xb8\xad\xe5\x9b\xbd\xe4\xba\xa7\xe5\xa6\x87\xe4\xb8\x93\xe7\x94\xa8\xe7\xba\xb8\xe7\x9a\x84\xe9\xa2\x86\xe5\x86\x9b\xe5\x93\x81\xe7\x89\x8c\xe3\x80\x82\xe6\xa2\x85\xe7\xac\x9b\xe6\x97\xb6\xe5\x88\xbb\xe5\x8a\x9b\xe6\xb1\x82\xe5\x88\x9b\xe6\x96\xb0\xe5\x92\x8c\xe8\xbf\x9b\xe6\xad\xa5\xef\xbc\x8c\xe5\xb9\xb6\xe4\xbb\xa5\xe6\x95\x8f\xe9\x94\x90\xe7\x9a\x84\xe7\x9b\xae\xe5\x85\x89\xe6\xb4\x9e\xe5\xaf\x9f\xe5\xb8\x82\xe5\x9c\xba\xe9\x9c\x80\xe6\xb1\x82\xef\xbc\x8c\xe4\xba\xa7\xe5\x93\x81\xe6\x8e\xa8\xe9\x99\x88\xe5\x87\xba\xe6\x96\xb0\xe4\xbb\xa5\xe6\xbb\xa1\xe8\xb6\xb3\xe6\xb6\x88\xe8\xb4\xb9\xe8\x80\x85\xe4\xb8\x8d\xe6\x96\xad\xe5\x8f\x98\xe5\x8c\x96\xe7\x9a\x84\xe9\x9c\x80\xe6\xb1\x82\xe3\x80\x82\xe9\x99\xa4\xe4\xba\x86\xe4\xb8\x93\xe6\xb3\xa8\xe5\x90\x91\xe6\xb6\x88\xe8\xb4\xb9\xe8\x80\x85\xe6\x8f\x90\xe4\xbe\x9b\xe6\xa2\x85\xe7\xac\x9b\xe4\xba\xa7\xe5\xa6\x87\xe4\xb8\x93\xe7\x94\xa8\xe5\x8d\xab\xe7\x94\x9f\xe7\xba\xb8\xe5\xa4\x96\xef\xbc\x8c\xe5\x85\xac\xe5\x8f\xb8\xe6\x96\xb0\xe8\xbf\x9b\xe4\xbc\x81\xe9\xb9\x85\xe7\x88\xb8\xe7\x88\xb8\xe7\xb3\xbb\xe5\x88\x97\xe6\xaf\x8d\xe5\xa9\xb4\xe7\x94\xa8\xe5\x93\x81\xef\xbc\x8c\xe5\xb9\xb6\xe9\x9d\xa2\xe5\x90\x91\xe5\x85\xa8\xe5\x9b\xbd\xe6\x8b\x9b\xe5\x95\x86\xe3\x80\x82\xe6\xad\xa3\xe6\x98\xaf\xe8\xbf\x99\xe7\xa7\x8d\xe5\x88\x9b\xe6\x96\xb0\xe7\x9a\x84\xe7\xb2\xbe\xe7\xa5\x9e\xe5\x92\x8c\xe8\xb4\xb4\xe5\xbf\x83\xe7\x9a\x84\xe6\x9c\x8d\xe5\x8a\xa1\xef\xbc\x8c\xe4\xbd\xbf\xe6\xa2\x85\xe7\xac\x9b\xe4\xb8\x80\xe7\x9b\xb4\xe5\xb9\xbf\xe5\x8f\x97\xe6\xac\xa2\xe8\xbf\x8e\xef\xbc\x8c\xe5\x9c\xa8\xe6\xb6\x88\xe8\xb4\xb9\xe8\x80\x85\xe4\xb8\xad\xe8\xb5\xa2\xe5\xbe\x97\xe4\xba\x86\xe9\xab\x98\xe5\xba\xa6\xe7\x9a\x84\xe5\x93\x81\xe7\x89\x8c\xe5\xbf\xa0\xe8\xaf\x9a\xe5\xba\xa6\xe5\x92\x8c\xe7\xbe\x8e\xe8\xaa\x89\xe5\xba\xa6\xe3\x80\x82\r\n      \xe2\x80\x9c\xe6\xa2\x85\xe7\xac\x9b\xe2\x80\x9d\xe6\x9b\xb4\xe6\x87\x82\xe4\xba\xa7\xe5\xa6\x87\xe9\x9c\x80\xe8\xa6\x81\xef\xbc\x8c\xe4\xba\xa7\xe5\xa6\x87\xe8\x88\x92\xe9\x80\x82\xef\xbc\x8c\xe5\x85\xa8\xe5\xae\xb6\xe5\xae\x89\xe5\xbf\x83\xe3\x80\x82\r\n\xe3\x80\x80\xe3\x80\x80\xe6\xa2\x85\xe7\xac\x9b\xe5\xb0\x86\xe7\xbb\xa7\xe7\xbb\xad\xe5\x8a\xaa\xe5\x8a\x9b\xe4\xb8\x8d\xe6\x87\x88\xef\xbc\x8c\xe7\x94\xa8\xe4\xb8\x93\xe4\xb8\x9a\xe7\x9a\x84\xe6\x8a\x80\xe6\x9c\xaf\xe3\x80\x81\xe4\xb8\x80\xe6\xb5\x81\xe7\x9a\x84\xe4\xba\xa7\xe5\x93\x81\xe3\x80\x81\xe5\x8a\xa1\xe5\xae\x9e\xe7\x9a\x84\xe6\x80\x81\xe5\xba\xa6\xef\xbc\x8c\xe6\x88\x90\xe9\x95\xbf\xe4\xb8\xba\xe5\x8d\xab\xe7\x94\x9f\xe7\x94\xa8\xe5\x93\x81\xe9\xa2\x86\xe5\x9f\x9f\xe5\x86\x89\xe5\x86\x89\xe5\x8d\x87\xe8\xb5\xb7\xe7\x9a\x84\xe6\x96\xb0\xe6\x98\x9f\xe3\x80\x82\xe6\xa2\x85\xe7\xac\x9b\xe5\x85\xb6\xe4\xbb\x96\xe4\xba\xa7\xe5\x93\x81\xe8\xbf\x98\xe6\x9c\x89b\xe8\xb6\x85\xe6\x93\xa6\xe6\x8b\xad\xe7\xba\xb8\xe3\x80\x81\xe5\x8e\x95\xe6\x89\x80\xe4\xb8\x93\xe7\x94\xa8\xe7\xba\xb8\xe3\x80\x81\xe5\x8e\xa8\xe7\xba\xb8\xe5\x8f\x8a\xe5\x85\xb6\xe4\xbb\x96\xe7\x9a\x84\xe5\xb8\xb8\xe8\xa7\x84\xe7\x94\x9f\xe6\xb4\xbb\xe7\x94\xa8\xe7\xba\xb8\xef\xbc\x88\xe8\xbd\xaf\xe6\x8a\xbd\xe3\x80\x81\xe7\x9b\x92\xe7\xba\xb8\xe3\x80\x81\xe6\x89\x8b\xe5\xb8\x95\xe7\xba\xb8\xe3\x80\x81\xe5\x8e\xa8\xe7\xba\xb8\xe3\x80\x81\xe6\xb9\xbf\xe5\xb7\xbe\xef\xbc\x89\xe7\xad\x89\r\n']
        #print s[0].encode('utf-8')
        #print 'ssssss %r' % s[0]

        self.headers = {
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip,deflate",
                        "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
                        "Connection": "keep-alive",
                        "Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
                        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36",
                        "Referer": "https://vip.1688.com/mc/index.htm"
        }

        self.cookies = {
                    'cna':'4mZNEIZEhQkCAXDmySPTzMtO',
                    'ali_beacon_id':'112.230.201.35.1474595798224.922154.5', 
                    'ali_apache_track':'c_ms=1|c_mid=b2b-768874955|c_lid=%E4%B8%8B%E4%B8%80%E4%B8%AA%E5%A4%A9%E4%BA%AE_1992',
                    'h_keys':'%u6d4e%u5357%u536b%u751f%u7eb8#%u5e7f%u5dde%u5e02%u773c%u7f69#%u6d4e%u5357%u5e02%u526a%u5200#%u9b54%u517d#%u526a%u5200%u773c%u7f69#%u5e7f%u5dde#%u9a9e%u57ae%u7a9e%u752f%ufffd#%u5e7f#%u7b363#%u8cb04',
                    'JSESSIONID':'8L785Auu1-PFBXj7pyPKEC515IMF-0rPInAQ-5vJ',
                    'ali_apache_tracktmp':'c_w_signed=Y',
                    'LoginUmid':'4%2FpTb962Fst8sOoCualGGezJVLQJh3uSw515gKXgZvpTG4BC5yy9jw%3D%3D', 
                    '__cn_logon__':'true',
                    '__cn_logon_id__':'%E4%B8%8B%E4%B8%80%E4%B8%AA%E5%A4%A9%E4%BA%AE_1992',
                    'userID':'fjBb5uEXesWpnlrhRmKZDuOVhB78%2FeWcn46vdNzhDY06sOlEpJKl9g%3D%3D',
                    'tbsnid':'g8UyA4l6VDtKK0kYtS5BigfQbOAk2VXr7FcLhljLrRw6sOlEpJKl9g%3D%3D', 
                    'cn_tmp':'Z28mC+GqtZ2ngfMQwCaf2dxEPERa09s/jeSt0+ivbArT1NYoELjpokDweRyOoW9Dn520k/VIxzdpduF2Fb9qMjjmGT8Ob5EXqK4FToDsiPb23AhNVRTkz8yXXPhwzC/EkfsjqaWommy5e4A8KimNO+P9ut/49kBVCyMJTdmoEp2g17+IJUPescUhf4B+rdHdYldneOYv8+5m/sWXV9io5zVy8ln3aHk4DrEsQMIippKbPbfYyiw2ts5LNN6XptptSwhXUirOF5s=',
                    'unb':'768874955',
                    'last_mid':'b2b-768874955',
                    '_cn_slid_':'W8th4Q2gpr', 
                    '__last_loginid__':'%E4%B8%8B%E4%B8%80%E4%B8%AA%E5%A4%A9%E4%BA%AE_1992', 
                    'login':'kFeyVBJLQQI%3D',
                    '_csrf_token':'1486695901199', 
                    '_is_show_loginId_change_block_':'b2b-768874955_false',
                    '_show_force_unbind_div_':'b2b-768874955_false',
                    '_show_sys_unbind_div_':'b2b-768874955_false',
                    '_show_user_unbind_div_':'b2b-768874955_false',
                    'ad_prefer':'2017/02/08 15:05:52',
                    'ali_ab':'113.128.146.72.1473477298123.8',
                    'userIDNum':'u8s2vIq9CsFTG4BC5yy9jw%3D%3D',
                    '_nk_':'3EoPeoqLhjl4HYvj4KFwiw%3D%3D',
                    '__rn_alert__':'false', 
                    '_tmp_ck_0':'HCGgddy%2F7BCpxElsrViZD6tusgof%2FQdxi7HyyxxXMfiUC%2FF5OpcprD52WazSgIPKMuL8eTrpZdAxaAQkB08%2FppeeZm7U%2BCpGYUT%2BuVBafC%2Fxatjx6yxVBW8EkO6PvdxWE6SYVhpQps9kyK1vyPsybB8IHMOYrk5MLWcq8aNKrx6R2RbVUVo2m%2BOW2tNUpeGJYNuPkvGGSyceWUrsumjXFpY3bMdorxc4MA1flVBke9d9EXGYxyenJOZDN9PvAZaVbImUBj%2FAnVVrdiZyvAvDDky4XechgMCAIh7XID%2BrMimnEZOdfc%2BDrTYhTC3aC4zJuLHmjucfq6JvS%2BI1JtivTv8g38CwJ70X8YnflUXs4ETMJ1bLmkNtgwDhK%2BVmY5v8HR1%2Fun8cuBlKtKA3jeIhCy1N2C1%2FAOx1XS51yfiWCxZ8ccR9KXM%2BMqoHhaM%2Blv398rlla%2BEWUHZSdnMsFqO8USiS6mPWp%2BYWHPiMWCA86DXEhR5cqxDlkcqOASNW4voWsuzmgVySTqp6lQO7YLE2m3nQV%2FZzKgozcDhEGIfSAx9VGyeTMWzeEg%3D%3D',
                    'alicnweb':'touch_tb_at%3D1486695904678%7Clastlogonid%3D%25E4%25B8%258B%25E4%25B8%2580%25E4%25B8%25AA%25E5%25A4%25A9%25E4%25BA%25AE_1992',
                    'l':'Ajc32CQUNeHjkgzTQuWbq3N3RyGAvQte',
                    'isg':'AkdHquNV00NLT1fPJKpCWh6t1v2YRhsuhnGkUxk1Ilb9iGVKIBmsftmKXP8s'
        }

    def start_requests(self):
        url = "https://s.1688.com/company/company_search.htm?keywords="+self.keyword+self.keyword2
        return [FormRequest(url,cookies=self.cookies,headers = self.headers,callback=self.after_login)]

    def after_login(self, response):
        split_coms = ''
        for sel in response.xpath('//div[1]/div[2]/div[3]/div[1]/div[4]/a[3]'):
            level_url = sel.xpath('@href').extract()
            utf8string = level_url[0].encode("utf-8")
            pattern = re.compile('company_site')
            match = re.search(pattern,utf8string)
            if match:
                print "未开店铺的Url>>>> %s" % match.group(0)
            else:
                split_coms = utf8string.replace('merchants','creditdetail')
                #time.sleep(6)
                yield scrapy.Request(split_coms ,cookies=self.cookies,headers = self.headers,callback=self.detail_login)
        #next_url = response.xpath('//*[@id="sw_mod_pagination_content"]/div/a[6]//@href').extract()
        #if len(next_url) > 0:
            #yield scrapy.Request(next_url[0] ,cookies=self.cookies,headers = self.headers,callback=self.after_login)
        #print "下一层url %s" % split_coms

    def detail_login(self, response):
        for sel in response.xpath('//*[@id="J_COMMON_CompanyInfoDetailInfo"]/span'):
            title = sel.xpath('text()').extract()
            #print "公司简介1 %r>>>>>" % title[0]
            #title_res = title[0].encode('utf-8')
            #print "公司简介2 %r>>>>>" % title_res
            items = SupplierItem()
            items['desc'] = title
            yield items
