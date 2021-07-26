# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter

from .items import CommentsItem, PostsItem, ComposersItem, CopyrightsItem


class VcatchPipeline:
    def open_spider(self, spider):
        self.db = pymysql.connect(
            user='root',
            password='Lisixiang0304!',
            database='xpc_2022'
        )
        self.cur = self.db.cursor()

    def process_item(self, item, spider):
        if isinstance(item, PostsItem):
            sql = f'insert into posts values(' \
                  f'"{item["pid"]}",' \
                  f'"{item["title"]}",' \
                  f'"{item["thumbnail"]}",' \
                  f'"{item["preview"]}",' \
                  f'"{item["video"]}",' \
                  f'"{item["video_format"]}",' \
                  f'"{item["category"]}",' \
                  f'"{item["duration"]}",' \
                  f'"{item["created_at"]}",' \
                  f'"{item["description"]}",' \
                  f'"{item["play_counts"]}",' \
                  f'"{item["like_counts"]}")'

        elif isinstance(item, CommentsItem):
            sql = f'insert into comments values(' \
                  f'{item["commentid"]},' \
                  f'{item["pid"]},' \
                  f'{item["cid"]},' \
                  f'"{item["avatar"]}",' \
                  f'"{item["uname"]}",' \
                  f'"{item["created_at"]}",' \
                  f'"{item["content"]}",' \
                  f'"{item["like_counts"]}",' \
                  f'"{item["reply"]}")'

        elif isinstance(item, ComposersItem):
            sql = f'insert into composers values(' \
                  f'"{item["cid"]}",' \
                  f'"{item["banner"]}",' \
                  f'"{item["avatar"]}",' \
                  f'"{item["verified"]}",' \
                  f'"{item["name"]}",' \
                  f'"{item["intro"]}",' \
                  f'"{item["like_counts"]}",' \
                  f'"{item["fans_counts"]}",' \
                  f'"{item["follow_counts"]}",' \
                  f'"{item["location"]}",' \
                  f'"{item["career"]}")'

        elif isinstance(item, CopyrightsItem):
            sql = f'insert into copyrights values(' \
                  f'"{item["pcid"]}",' \
                  f'"{item["pid"]}",' \
                  f'"{item["cid"]}",' \
                  f'"{item["roles"]}")'

        try:
            self.cur.execute(sql)
            self.db.commit()
        except Exception as e:
            print("insert failed ...", e)
            self.db.rollback()
        else:
            print("insert successful !")

        return item

    def close_spider(self, spider):
        self.cur.close()
        self.db.close()
