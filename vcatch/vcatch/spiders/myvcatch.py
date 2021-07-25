import json

import scrapy
from ..items import *


class MyvcatchSpider(scrapy.Spider):
    name = 'myvcatch'
    allowed_domains = ['xinpianchang.com']
    start_urls = ['https://www.xinpianchang.com/channel/index/sort-like?from=navigator']

    def parse(self, response, **kwargs):
        li_list = response.xpath('//ul[@class="video-list"]/li')
        for li in li_list:
            pid = li.xpath('./@data-articleid').get()
            title = li.xpath('.//div[@class="video-con-top"]/a/p/text()').get()
            thumbnail = li.xpath('./a/img/@_src').get()
            category = ','.join(
                li.xpath('.//div[@class="new-cate"]/span[@class="fs_12 fw_300 c_b_9"]/text()').getall()).replace('\t',
                                                                                                                 '').replace(
                '\n', '').replace(' ', '')
            duration = li.xpath('./a/span/text()').get()
            created_at = li.xpath('.//div[@class="video-hover-con"]/p/text()').get()

            # item class encapsulates
            post_item = PostsItem(
                pid=pid,
                title=title,
                thumbnail=thumbnail,
                category=category,
                # duration=duration,
                created_at=created_at
            )

            # request details
            post_url = f'https://www.xinpianchang.com/a{pid}?from=ArticleList'
            yield scrapy.Request(
                url=post_url,
                callback=self.parse_detail,
                meta={'post_item': post_item}
            )

    def parse_detail(self, response):
        post_item = response.meta['post_item']
        description = response.xpath(
            '//p[@class="desc line-hide fs_14 c_b_3 fw_300 line-hide-3"]/text()').get().replace('\t', '')
        play_counts = response.xpath('//i[@class="fs_12 fw_300 c_b_6 v-center play-counts"]/@data-curplaycounts').get()
        like_counts = response.xpath('//span[@class="v-center like-counts fs_12 c_w_f fw_300 show"]/@data-counts').get()

        '''
        video data ---> json format
        https://mod-api.xinpianchang.com/mod/api/v2/media/xn2k9QALWvg418MZ?appKey=61a2f329348b3bf77&extend=userInfo%2CuserStatus
        https://mod-api.xinpianchang.com/mod/api/v2/media/MDA96QeNbdx7j5N0?appKey=61a2f329348b3bf77&extend=userInfo%2CuserStatus
        https://mod-api.xinpianchang.com/mod/api/v2/media/P8pvbQYa2mpQ306X?appKey=61a2f329348b3bf77&extend=userInfo%2CuserStatus
        observe differences
        get vid from element after checking the url
        the reason is to DYNAMICALLY get the source of the video
        we cant directly get from url because it was provided by Ajax
        '''

        vid = response.xpath('//a[@class="collection-star hollow-star"]/@data-vid').get()
        video_url = f'https://mod-api.xinpianchang.com/mod/api/v2/media/{vid}?appKey=61a2f329348b3bf77&extend=userInfo%2CuserStatus'

        # update post_item
        post_item['description'] = description
        post_item['play_counts'] = play_counts
        post_item['like_counts'] = like_counts

        yield scrapy.Request(
            url=video_url,
            callback=self.parse_video,
            meta={'post_item': post_item}
        )

    def parse_video(self, response):
        post_item = response.meta['post_item']

        # parse json
        content = response.json()

        # get data from json, detailed json see video_info.json
        preview = content['data']['cover']
        duration = content['data']['duration']
        video = content['data']['resource']['progressive'][2]['url']  # 1080p selected
        video_format = content['data']['resource']['progressive'][2]['mime']

        # append to post_item
        post_item['preview'] = preview
        post_item['duration'] = duration
        post_item['video'] = video
        post_item['video_format'] = video_format
        yield post_item

        # now we can go to pipelines
