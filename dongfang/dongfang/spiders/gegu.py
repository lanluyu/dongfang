# -*- coding: utf-8 -*-
from scrapy import Request,Spider
from dongfang.items import DongfangItem


class GeguSpider(Spider):
    name = 'gegu'
    allowed_domains = ['http://data.eastmoney.com/']
    start_url = 'http://data.eastmoney.com/stockcomment/'

    def start_requests(self):
        for page in range(1,75):
            yield Request(url=self.start_url,callback=self.parse,meta={'page':page},dont_filter=True)

    def parse(self, response):
        # print(response.text)
        a = response.xpath('.//span[@class="at"]/text()').extract_first()
        print('正在爬取',a,'页')
        # 定位到想要提取信息的父元素
        stocks = response.xpath('.//table[@cellpadding="0"]/tbody/tr')
        for stock in stocks:
            item = DongfangItem()
            item['stock_code'] = ''.join(stock.xpath('.//td[@class="col"]/a/text()').extract())
            item['stock_name'] = ''.join(stock.xpath('.//td[3]/a/text()').extract())
            item['stock_price'] = ''.join(stock.xpath('.//td[5]/span/text()').extract())   
            item['stock_clickspan'] = ''.join(stock.xpath('.//td[8]/text()').extract())         
            item['stock_institutions'] = ''.join(stock.xpath('.//td[10]/text()').extract())  
            item['stock_cost'] = ''.join(stock.xpath('.//td[9]/text()').extract())
            item['stock_tieba'] = ''.join(stock.xpath('.//td/a[3]/@href').extract())
            item['stock_report'] = ''.join(stock.xpath('.//td/a[4]/@href').extract())   

            yield item
            print(item)
