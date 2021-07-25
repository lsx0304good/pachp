import scrapy
from ..items import MeijuItem

class MeijuspiderSpider(scrapy.Spider):
    name = 'meijuSpider'
    allowed_domains = ['meijutt.tv']
    start_urls = ['https://www.meijutt.tv/new100.html']

    def parse(self, response, **kwargs):
        pass
        # print("*" * 50)
        # print(response.text)  # text
        # print(response.body)  # binary
        # print(response.json())  # json parse
        # print("*" * 50)

        # XPath parse
        li_list = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        for li in li_list:
            vname = li.xpath('./h5/a/text()').get()
            # movie_name = li.xpath('./h5/a/text()').getall()  # will return a list
            vtype = li.xpath('./span[@class="mjjq"]/text()').get()
            vsrc = li.xpath('./span[@class="mjtv"]/text()').get()

            yield MeijuItem(vname=vname, vtype=vtype, vsrc=vsrc)


# scrapy startproject projectname
# scrapy genspider spidername domain
# scrapy crawl spidername
