# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3


class MyprojectPipeline(object):
    
    CREATE_TABLE=('create table review ('
        'id integer primary key,'
        'user_name text,'
        'age text,'
        'sex text,'
        'product_name text,'
        'evaluation integer,'
        'date text,'
        'title text,'
        'contents text,'
        'helpfulnum integer'
    ')')

    INSERT_DATA=('insert into review ('
        'user_name,age,sex,product_name,'
        'evaluation,date,title,contents,helpfulnum'
    ') values ('
        '?,?,?,?,?,?,?,?,?'
    ')')

    DB_NAME='rakuten_scraping.db'
    conn=None

    def __init__(self):
        self.conn=sqlite3.connect(self.DB_NAME)
        if self.conn.execute("select count(*) from sqlite_master where name='review'").fetchone()[0] == 0:
            self.conn.execute(self.CREATE_TABLE)


    def open_sqider(self,spider):
        self.conn=sqlite3.connect(self.DB_NAME)


    def process_item(self, item, spider):
        if spider.name=='product_rakuten':
            self.conn.execute(self.INSERT_DATA,(
                item['user_name'],item['age'],item['sex'],
                item['product_name'],
                item['evaluation'],item['date'],item['title'],
                item['contents'],item['helpfulnum']
            ))
        self.conn.commit()        
        return item
    
    def close_spider(self,spider):

        self.conn.close()
