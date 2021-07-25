# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MeijuItem(scrapy.Item):
    # define the fields for your item here like:
    vname = scrapy.Field()
    vtype = scrapy.Field()
    vsrc = scrapy.Field()
    pass
