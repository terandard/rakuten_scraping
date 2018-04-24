import scrapy

from myproject.items import Review

class RakutenSpider(scrapy.Spider):
    name = 'rakuten' #Spiderの名前
    # クロール対象とするドメインのリスト
    allowed_domains = ['review.rakuten.co.jp']
    # クロールを開始するURLのリスト。
    # 1要素のタプルの末尾にはカンマが必要。
    #""https://review.rakuten.co.jp/item/1/213310_14507231/1.1/
    #'http://review.rakuten.co.jp/'
    #https://review.rakuten.co.jp/item/1/213310_18886289/1.1/
    start_urls = ["https://review.rakuten.co.jp/item/1/213310_14507231/1.1/"]

    def parse(self, response):
        product_name=response.css("h2.revItemTtl.fn span a::text").extract_first()
        for ureview in response.css("div.revRvwUserSec.hreview"):
            item=Review()
            """
            #user_name
            print(ureview.css("dt.revUserFaceName.reviewer a::text").extract_first())
            #age,sex
            print(ureview.css("span.revUserFaceDtlTxt span::text").extract_first())
            #review_num
            print(ureview.css("span.revUserFaceDtlTxt span a::text").extract_first())
            #evaluation
            print(ureview.css("span.revUserRvwerNum.value::text").extract_first())
            #date
            print(ureview.css("span.revUserEntryDate.dtreviewed::text").extract_first())
            #purpose,user,frequence
            print(ureview.css("span.revDispListTxt::text").extract())
            #title
            print(ureview.css("dt.revRvwUserEntryTtl::text").extract_first())
            #review
            print(ureview.css("dd.revRvwUserEntryCmt::text").extract())
            #helpfullnum
            print(ureview.css("span.revEntryAnsNum::text").extract_first())
            print("*******************************\n")
            """
            temp=ureview.css("dt.revUserFaceName.reviewer a::text").extract_first()
            if temp==None:
                item['user_name']='購入者'
                item['age']='null'
                item['sex']='null'
                item['review_num']='null'
            else:
                item['user_name']=temp
                item['age']=ureview.css("span.revUserFaceDtlTxt span::text").extract_first().split(' ')[0]
                item['sex']=ureview.css("span.revUserFaceDtlTxt span::text").extract_first().split(' ')[1]
                item['review_num']=ureview.css("span.revUserFaceDtlTxt span a::text").extract_first()
            temp=ureview.css("span.revDispListTxt::text").extract()
            if not temp or len(temp)!=3:
                item['purpose']='null'
                item['user']='null'
                item['frequency']='null'
            else:
                item['purpose']=temp[0]
                item['user']=temp[1]
                item['frequency']=temp[2]
            item['evaluation']=ureview.css("span.revUserRvwerNum.value::text").extract_first()
            item['date']=ureview.css("span.revUserEntryDate.dtreviewed::text").extract_first()
            item['title']=ureview.css("dt.revRvwUserEntryTtl::text").extract_first()
            temp=ureview.css("dd.revRvwUserEntryCmt::text").extract()
            item['contents']=' '.join(temp)
            temp=ureview.css("span.revEntryAnsNum::text").extract_first()
            if temp==None:
                item['helpfullnum']=0
            else:
                item['helpfullnum']=temp
            item['product_name']=product_name
            yield item

        try:
            next_page=response.css('div.revPagination a::attr(href)')[-1].extract()
            next_page=response.urljoin(next_page)
            yield scrapy.Request(next_page,callback=self.parse)
        except IndexError:
            print('end\n')

