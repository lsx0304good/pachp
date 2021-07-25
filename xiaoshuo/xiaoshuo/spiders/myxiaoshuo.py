import scrapy
from ..items import *


class MyxiaoshuoSpider(scrapy.Spider):
    name = 'myxiaoshuo'
    allowed_domains = ['b520.org']
    start_urls = ['http://www.b520.org/xuanhuanxiaoshuo/']

    def parse(self, response, **kwargs):
        li_list = response.xpath('//div[@class="l"]/ul/li')
        for li in li_list:
            xs_name = li.xpath('./span[@class="s2"]/a/text()').get()
            xs_url = li.xpath('./span[@class="s2"]/a/@href').get()

            # 请求章节
            yield scrapy.Request(
                url=xs_url,
                callback = self.parse_detail,
                meta={'xs_name': xs_name}
            )

    def parse_detail(self, response):
        xs_name = response.meta.get('xs_name')

        dd_list = response.xpath('//div[@id="list"]/dl/dd')
        for dd in dd_list:
            zj_name = dd.xpath('./a/text()').get()
            zj_url = dd.xpath('./a/@href').get()

            # 请求章节内容
            yield scrapy.Request(
                url=zj_url,
                callback=self.parse_content,
                meta={
                    'xs_name': xs_name,
                    'zj_name': zj_name,
                }
            )

    def parse_content(self, response):
        xs_name = response.meta.get('xs_name')
        zj_name = response.meta.get('zj_name')

        p_list = response.xpath('//div[@id="content"]/p/text()').getall()
        zj_content = '\n'.join(p_list)

        yield XiaoshuoItem(
            xs_name=xs_name,
            zj_name=zj_name,
            zj_content=zj_content,
        )



