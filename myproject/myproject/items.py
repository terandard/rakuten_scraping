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


class Review(scrapy.Item):
    user_name=scrapy.Field()
    age=scrapy.Field()
    sex=scrapy.Field()
    review_num=scrapy.Field()
    product_name=scrapy.Field()
    purpose=scrapy.Field()
    user=scrapy.Field()
    frequency=scrapy.Field()
    evaluation=scrapy.Field()
    date=scrapy.Field()
    title=scrapy.Field()
    contents=scrapy.Field()
    helpfullnum=scrapy.Field()

class Product(scrapy.Item):
    product_id=scrapy.Field()
    product_name=scrapy.Field()
    author=scrapy.Field()
    abstract=scrapy.Field()
    user_evaluation=scrapy.Field()
    price=scrapy.Field()
    category=scrapy.Field()
    review_num=scrapy.Field()