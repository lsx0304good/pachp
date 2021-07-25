import scrapy
from ..items import *


class MysinaSpider(scrapy.Spider):
    name = 'mysina'
    allowed_domains = ['news.sina.com.cn']
    start_urls = ['http://roll.news.sina.com.cn/news/gnxw/gdxw1/index_1.shtml']

    # initialize page num
    page = 1

    def parse(self, response, **kwargs):
        # print(response.text)
        li_list = response.xpath('//ul[@class="list_009"]/li')
        for li in li_list:
            ntitle = li.xpath('./a/text()').get().replace('"', '')
            ntime = li.xpath('./span/text()').get().replace('"', '')

            yield SinaItem(ntitle=ntitle, ntime=ntime)


        while self.page < 3:
            self.page += 1
            url = f'http://roll.news.sina.com.cn/news/gnxw/gdxw1/index_{self.page}.shtml'
            yield scrapy.Request(url=url, callback=self.parse)


