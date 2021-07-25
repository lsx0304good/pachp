# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaoshuoItem(scrapy.Item):
    # define the fields for your item here like:
    xs_name = scrapy.Field()
    zj_name = scrapy.Field()
    zj_content = scrapy.Field()
