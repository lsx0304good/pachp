import pymysql
import redis
import time
import json

# 1. 从redis中取出 mybaike:items列表中的数据
# 2. 然后插入到MySQL的tb_baike表中

# 连接MySQL
db = pymysql.connect(user='root', password='Lisixiang0304!', database='pachong')
cur = db.cursor()

# 连接redis
r = redis.Redis()

while True:
    # 从redis中取出数据
    # blpop() : 从列表的左边取出第一个元素，如果没有数据了会暂停等待数据
    key, val = r.blpop('mybaike:items')
    # print(key, val)
    # b'mybaike:items' b'{"title": "\\u7f8e\\u56fd\\u7ecf\\u6d4e\\u8bc4\\u8bba"}'

    # json解析
    item = json.loads(val.decode())

    # 写入MySQL
    sql = f'insert into baike(title) values("{item["title"]}")'
    cur.execute(sql)
    db.commit()

    print(f' ---- 插入成功: {item["title"]} ----')

    time.sleep(0.1)



