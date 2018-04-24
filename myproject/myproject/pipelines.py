# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3


class MyprojectPipeline(object):
    CREATE_TABLE=('create table rakuten_review ('
        'id integer primary key,'
        'user_name text,'
        'age text,'
        'sex text,'
        'review_num integer,'
        'product_name text,'
        'purpose text,'
        'user text,'
        'frequency text,'
        'evaluation integer,'
        'date text,'
        'title text,'
        'contents text,'
        'helpfullnum integer'
    ')')
    
    CREATE_TABLE_book=('create table dvd_review ('
        'id integer primary key,'
        'user_name text,'
        'age text,'
        'sex text,'
        'product_name text,'
        'evaluation integer,'
        'date text,'
        'title text,'
        'contents text,'
        'helpfullnum integer'
    ')')

    INSERT_DATA=('insert into rakuten_review ('
        'user_name,age,sex,review_num,'
        'product_name,purpose,user,frequency,'
        'evaluation,date,title,contents,helpfullnum'
    ') values ('
        '?,?,?,?,?,?,?,?,?,?,?,?,?'
    ')')

    INSERT_book_DATA=('insert into dvd_review ('
        'user_name,age,sex,product_name,'
        'evaluation,date,title,contents,helpfullnum'
    ') values ('
        '?,?,?,?,?,?,?,?,?'
    ')')

    DB_NAME='../hdd/DB/rakuten_scraping.db'
    conn=None

    def __init__(self):
        self.conn=sqlite3.connect(self.DB_NAME)
        if self.conn.execute("select count(*) from sqlite_master where name='rakuten_review'").fetchone()[0] == 0:
            self.conn.execute(self.CREATE_TABLE)
        if self.conn.execute("select count(*) from sqlite_master where name='dvd_review'").fetchone()[0] == 0:
            self.conn.execute(self.CREATE_TABLE_book)


    def open_sqider(self,spider):
        self.conn=sqlite3.connect(self.DB_NAME)


    def process_item(self, item, spider):
        if spider.name=='rakuten':
            self.conn.execute(self.INSERT_DATA,(
                item['user_name'],item['age'],item['sex'],
                item['review_num'],item['product_name'],
                item['purpose'],item['user'],item['frequency'],
                item['evaluation'],item['date'],item['title'],
                item['contents'],item['helpfullnum']
            ))
        """
        """
        if spider.name=='product_rakuten':
            self.conn.execute(self.INSERT_book_DATA,(
                item['user_name'],item['age'],item['sex'],
                item['product_name'],
                item['evaluation'],item['date'],item['title'],
                item['contents'],item['helpfullnum']
            ))
        self.conn.commit()        
        return item
    
    def close_spider(self,spider):

        self.conn.close()
