# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field, Item


# article item
class PostsItem(Item):
    pid = Field()
    title = Field()
    thumbnail = Field()
    preview = Field()
    video = Field()
    video_format = Field()
    category = Field()
    duration = Field()
    created_at = Field()
    description = Field()
    play_counts = Field()
    like_counts = Field()


class ComposersItem(Item):
    cid = Field()
    banner = Field()
    avatar = Field()
    verified = Field()
    name = Field()
    intro = Field()
    like_counts = Field()
    fans_counts = Field()
    follow_counts = Field()
    location = Field()
    career = Field()


class CommentsItem(Item):
    commentid = Field()
    pid = Field()
    cid = Field()
    avatar = Field()
    uname = Field()
    created_at = Field()
    content = Field()
    like_counts = Field()
    reply = Field()


class CopyrightsItem(Item):
    pcid = Field()  # pid_cid
    pid = Field()
    cid = Field()
    roles = Field()

