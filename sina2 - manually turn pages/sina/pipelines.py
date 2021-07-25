# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter


class SinaPipeline:
    def open_spider(self, spider):
        self.db = pymysql.connect(user='root', password='Lisixiang0304!', database='pachong')
        self.cur = self.db.cursor()

    def process_item(self, item, spider):
        sql = f'insert into sina_news(ntitle, ntime) values ("{item["ntitle"]}", "{item["ntime"]}")'
        try:
            self.cur.execute(sql)
            self.db.commit()
        except Exception as e:
            print("insert failed", e)
            self.db.rollback()
        else:
            print("insert successful!")

        return item

    def close_spider(self, spider):
        self.cur.close()
        self.db.close()
