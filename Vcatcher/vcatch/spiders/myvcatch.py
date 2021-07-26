import json

import scrapy
from ..items import *
import re


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

        # comments data
        pid = post_item['pid']
        comment_url = f'https://app2.xinpianchang.com/comments?resource_id={pid}&type=article&page=1&per_page=24&_=1627263351271'
        yield scrapy.Request(
            url=comment_url,
            callback=self.parse_comment
        )

        # creators data
        li_list = response.xpath('//*[@class="filmplay-creator right-section"]/ul/li')
        for li in li_list:
            cid = li.xpath('./a/@data-userid').get()

            # request data from creator page
            composer_url = li.xpath('./a/@href').get()
            composer_url = 'https://www.xinpianchang.com' + composer_url

            composer_item = ComposersItem(
                cid=cid
            )

            yield scrapy.Request(
                url=composer_url,
                callback=self.parse_composer,
                meta={'composer_item': composer_item}
            )

            # copyrights data
            roles = li.xpath('//*[@class="roles fs_12 fw_300 c_b_9"]/text()').get()
            yield CopyrightsItem(
                pcid=f'{pid}_{cid}',
                pid=pid,
                cid=cid,
                roles=roles
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

    def parse_comment(self, response):
        content = response.json()
        comment_list = content['data']['list']
        for comment in comment_list:
            commentid = comment['id']
            pid = comment['resource_id']
            cid = comment['userid']
            avatar = comment['userInfo']['avatar']
            uname = comment['userInfo']['username']
            created_at = comment['addtime']
            content = comment['content']
            like_counts = comment['count_approve']
            reply = comment['referid']

            yield CommentsItem(
                commentid=commentid,
                pid=pid,
                cid=cid,
                avatar=avatar,
                uname=uname,
                created_at=created_at,
                content=content,
                like_counts=like_counts,
                reply=reply
            )

    def parse_composer(self, response):
        # first, get passed data
        composer_item = response.meta['composer_item']

        banner = response.xpath('//*[@class="banner-wrap"]/@style').get()
        banner = re.findall('background-image:url\((.*?)\)', banner)[0]

        avatar = response.xpath('//*[@class="avator-wrap-s"]/img/@src').get()
        verified = "Yes" if response.xpath('//*[@class="avator-wrap-s"]/span').get() else "No"

        name = response.xpath('//*[@class="creator-name fs_26 fw_600 c_b_26"]/text()').get().replace('\t', '')
        intro = response.xpath('//*[@class="creator-desc fs_14 fw_300 c_b_3 line-hide-1"]/text()').get()
        like_counts = response.xpath('//*[@class="like-counts fw_600 v-center"]/text()').get().replace(',', '')
        fans_counts = response.xpath('//*[@class="fans-counts fw_600 v-center"]/@data-counts').get()
        follow_counts = response.xpath('//*[@class="fw_600 v-center"]/text()').get().replace(',', '')

        location = response.xpath('//*[@class="icon-location v-center"]/following-sibling::*/text()').get()
        location = location if location else ''

        career = response.xpath('//*[@class="icon-career v-center"]/following-sibling::*/text()').get()
        career = career if career else ''

        composer_item['banner'] = banner
        composer_item['avatar'] = avatar
        composer_item['verified'] = verified
        composer_item['name'] = name
        composer_item['intro'] = intro
        composer_item['like_counts'] = like_counts
        composer_item['fans_counts'] = fans_counts
        composer_item['follow_counts'] = follow_counts
        composer_item['location'] = location
        composer_item['career'] = career

        yield composer_item

