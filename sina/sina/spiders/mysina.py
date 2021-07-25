import scrapy
from ..items import *


class MysinaSpider(scrapy.Spider):
    name = 'mysina'
    allowed_domains = ['news.sina.com.cn']
    start_urls = ['http://roll.news.sina.com.cn/news/gnxw/gdxw1/index_1.shtml']

    def parse(self, response, **kwargs):
        # print(response.text)
        li_list = response.xpath('//ul[@class="list_009"]/li')
        for li in li_list:
            ntitle = li.xpath('./a/text()').get()
            ntime = li.xpath('./span/text()').get()

            yield SinaItem(ntitle=ntitle, ntime=ntime)
