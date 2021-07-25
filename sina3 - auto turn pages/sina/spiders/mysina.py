import scrapy
from ..items import *

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class MysinaSpider(CrawlSpider):
    name = 'mysina'
    allowed_domains = ['news.sina.com.cn']
    start_urls = ['http://roll.news.sina.com.cn/news/gnxw/gdxw1/index_1.shtml']

    # rules
    rules = [
        Rule(
            LinkExtractor(
                allow=('index_\d+\.shtml',),
                restrict_xpaths=('//*[@class="pagebox"][1]',),
            ),
            callback='parse_item',
            follow=True,
        )
    ]

    def parse_item(self, response, **kwargs):
        # print(response.text)
        li_list = response.xpath('//ul[@class="list_009"]/li')
        for li in li_list:
            ntitle = li.xpath('./a/text()').get().replace('"', '')
            ntime = li.xpath('./span/text()').get().replace('"', '')

            yield SinaItem(ntitle=ntitle, ntime=ntime)
