# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZimukuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #要爬取的内容定义
    text = scrapy.Field()
