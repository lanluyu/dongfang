# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class DongfangItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    stock_code = Field()
    stock_name = Field()
    stock_price = Field()   
    stock_clickspan = Field()     # 市盈率    
    stock_institutions = Field()  # 机构参与度
    stock_cost = Field()
    stock_tieba = Field()
    stock_report = Field()
