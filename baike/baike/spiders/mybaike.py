# pip install scrapy-redis
from  scrapy_redis.spiders import RedisCrawlSpider

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from baike.items import *


class MybaikeSpider(RedisCrawlSpider):
    name = 'mybaike'
    allowed_domains = ['baike.baidu.com']

    # start_urls = ['https://baike.baidu.com/']
    # 使用 redis_key 替代start_urls
    # 指的是监听redis数据库中的 mybaike:start_urls 键
    redis_key = 'mybaike:start_urls'

    # rules
    rules = [
        Rule(
            LinkExtractor(
                # 找页面中所有a标签href属性值与下面的正则匹配的内容
                allow=('/item/.*?', )
            ),
            callback='parse_item',
            follow=True
        )
    ]

    def parse_item(self, response, **kwargs):
        pass
        # print('*' * 60)
        # print(len(response.text))
        # print('*' * 60)

        # xpath解析
        title = response.xpath('//dd[@class="lemmaWgt-lemmaTitle-title J-lemma-title"]/h1/text()').get()
        # print(title)

        # item
        yield BaikeItem(title=title)


# "mybaike:start_urls" : 第一次请求的url
# "mybaike:requests" : 待爬取的url请求
# "mybaike:dupefilter" : 过滤器：对url进行去重
# "mybaike:items" : 存储数据
