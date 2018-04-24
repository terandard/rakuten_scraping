import scrapy

from myproject.items import Product_review

class Product_rakutenSpider(scrapy.Spider):
    name = 'product_rakuten' #Spiderの名前
    # クロール対象とするドメインのリスト
    allowed_domains = ['product.rakuten.co.jp']
    # クロールを開始するURLのリスト。
    # 1要素のタプルの末尾にはカンマが必要。
    #'http://review.rakuten.co.jp/'
    #https://product.rakuten.co.jp/search/?s=7&id=101266&v=table&st=1
    #https://product.rakuten.co.jp/product/-/87cd9339b544746dac8cb871dcc18fc6/review/

    start_urls = ["https://product.rakuten.co.jp/search/?s=7&id=101354&v=table&st=1"]


    def parse(self, response):
        limit='2'
        for product in response.css('ul.proStarList li a::attr(href)').extract():
            #print(product)
            review_page=response.urljoin(product)
            yield scrapy.Request(review_page,callback=self.parse_item)
        try:
            now_page_num=response.css('span.thisPage::text').extract_first()
            print(now_page_num)
            if now_page_num!=limit:
                next_page_list=response.css('div.rsrPagination a::attr(href)')[-1].extract()
                next_page_list=response.urljoin(next_page_list)
                yield scrapy.Request(next_page_list,callback=self.parse)
            else:
                print('end\n')
        except IndexError:
            print('end\n')    
        """
        """

    def parse_item(self,response):
        product_name=response.css("div.topProduct__title span::text").extract_first()
        #print(product_name)
        for ureview in response.css("div.rpsRevList.clfx"):
            item=Product_review()
            temp=ureview.css("div.revName a::text").extract_first()
            if temp==None:
                item['user_name']='購入者'
                item['age']='null'
                item['sex']='null'
            else:
                item['user_name']=temp
                item['age']=ureview.css("div.revAges::text").extract_first().split('/')[0]
                item['sex']=ureview.css("div.revAges::text").extract_first().split('/')[1]
            item['evaluation']=ureview.css("span.txtPoint::text").extract_first()
            item['date']=ureview.css("div.revDays::text").extract_first()
            item['title']=ureview.css("div.revTitle font b::text").extract_first()
            temp=ureview.css("div.revTxt::text").extract()
            item['contents']=' '.join(temp)
            temp=ureview.css("div.revRef p span::text").extract_first()
            if temp==None:
                item['helpfullnum']=0
            else:
                item['helpfullnum']=temp
            item['product_name']=product_name
            yield item

        try:
            next_page=response.css('a.item.-next::attr(href)').extract_first()
            next_page=response.urljoin(next_page)
            yield scrapy.Request(next_page,callback=self.parse_item)
        except IndexError:
            print('end\n')
        """
        """

