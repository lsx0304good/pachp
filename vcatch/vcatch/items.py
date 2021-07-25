# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# article item
class PostsItem(scrapy.Item):
    pid = scrapy.Field()
    title = scrapy.Field()
    thumbnail = scrapy.Field()
    preview = scrapy.Field()
    video = scrapy.Field()
    video_format = scrapy.Field()
    category = scrapy.Field()
    duration = scrapy.Field()
    created_at = scrapy.Field()
    description = scrapy.Field()
    play_counts = scrapy.Field()
    like_counts = scrapy.Field()
