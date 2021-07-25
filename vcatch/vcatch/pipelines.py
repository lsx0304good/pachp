# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter


class VcatchPipeline:
    def open_spider(self, spider):
        self.db = pymysql.connect(
            user='root',
            password='Lisixiang0304!',
            database='xpc_2022'
        )
        self.cur = self.db.cursor()

    def process_item(self, item, spider):
        # insert records
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

        try:
            self.cur.execute(sql)
            self.db.commit()
        except Exception as e:
            print("insert failed ...", e)
            self.db.rollback()
        else:
            print("insert successful !")

    def close_spider(self, spider):
        self.cur.close()
        self.db.close()
