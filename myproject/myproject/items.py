# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Product_review(scrapy.Item):
    user_name=scrapy.Field()
    age=scrapy.Field()
    sex=scrapy.Field()
    product_name=scrapy.Field()
    evaluation=scrapy.Field()
    date=scrapy.Field()
    title=scrapy.Field()
    contents=scrapy.Field()
    helpfullnum=scrapy.Field()
