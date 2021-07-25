# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os

from itemadapter import ItemAdapter


class XiaoshuoPipeline:
    def process_item(self, item, spider):
        xs_name = item['xs_name']
        zj_name = item['zj_name']
        zj_content = item['zj_content']

        base_path = r'/Users/simon_li/Desktop/pachp/xiaoshuo/xiaoshuo/storefile'

        xs_path = os.path.join(base_path, xs_name)
        if not os.path.exists(xs_path):
            os.mkdir(xs_path)

        zj_path = os.path.join(xs_path, f'{zj_name}.txt')
        with open(zj_path, 'w', encoding='utf-8') as f:
            f.write(zj_content)
            f.flush()
        print(f'catching {xs_name} : {zj_name} ... ok')

        return item
