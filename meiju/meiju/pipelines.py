# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql as pymysql
from itemadapter import ItemAdapter


class MeijuPipeline:

    # 开始爬虫
    def open_spider(self, spider):
        print("start crawling ...")

        # CASE1 存储到文件
        # self.fp = open('meiju.txt', 'a', encoding='utf-8')

        # CASE2 存储到 MySQL
        self.db = pymysql.connect(user='root', password='Lisixiang0304!', database='pachong')
        self.cur = self.db.cursor()

    '''
    spider中yield一次，就会调用一次

    当前 process_item 的调用条件：
    1. parse 中要写 yield
    2. 在 settings 中配置管道

    '''

    def process_item(self, item, spider):
        # print('item:', item)
        # print(spider.name)  # meijuSpider类的爬虫对象

        # CASE1 存储到 文件
        # self.fp.write(f'{str(item)}\n')

        # CASE2 存储到 MySQL
        sql = f'insert into meiju(vname, vtype, vsrc) values ("{item["vname"]}", "{item["vtype"]}", "{item["vsrc"]}")'
        self.cur.execute(sql)  # 执行sql
        self.db.commit()  # 提交事务

        return item

    # 关闭爬虫
    def close_spider(self, spider):
        print("end crawling ...")

        # CASE1 存储到文件
        # self.fp.close()

        # CASE2 存储到 MySQL
        self.cur.close()
        self.db.close()
