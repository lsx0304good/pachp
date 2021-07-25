import re
import requests
from fake_useragent import UserAgent
from requests import Response


def get_data(url):
    headers = {
        'User-Agent': UserAgent().random
    }
    resp = requests.get(url=url, headers=headers)

    if resp.status_code == 200:
        parse_data(resp.text)
        # print(resp.text)


def parse_data(data):
    houses = re.findall(r"""
    <div.+?des.+?<h2>.+?<a.+?strongbox.+?>(.+?)</a>  # 房源标题
    .+?<p.+?room">(.+?)</p>  # 户型信息
    .+?<b.+?strongbox">(.+?)</b>  # 价格
    """, data, flags=re.VERBOSE | re.DOTALL)

    for h in houses:
        print(h)


def main():
    url = 'https://bj.58.com/chuzu/'
    get_data(url)


if __name__ == '__main__':
    main()

'''
findall()
使用 .+? 匹配无用数据
使用 (.+?) 匹配有用数据
flags=re.VERBOSE | re.DOTALL  可换行正则 + 匹配空格和换行
'''