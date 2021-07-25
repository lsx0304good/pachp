# API: http://dps.kdlapi.com/api/getdps/?orderid=962700851479875&num=5&pt=1&format=json&sep=1
# 用户名：772887864  密码：bc9k2sms
# ip: 111.197.236.2

"""使用requests请求代理服务器
请求http和https网页均适用
"""

import requests
import random
from fake_useragent import UserAgent

page_url = "https://movie.douban.com/top250"  # 要访问的目标网页
# API接口，返回格式为json
api_url = "http://dps.kdlapi.com/api/getdps/?orderid=962700851479875&num=5&pt=1&format=json&sep=1"

# API接口返回的ip
proxy_ip = requests.get(api_url).json()['data']['proxy_list']

# proxy_ip output sample
'''
{
  "msg": "",
  "code": 0,
  "data": {
    "count": 10,
    "dedup_count": 10,
    "order_left_count": 990,
    "proxy_list": [
      "124.172.117.189:19812",
      "219.133.31.120:26947",
      "183.237.194.145:28436",
      "183.62.172.50:23485",
      "163.125.157.243:17503",
    ]
  }
}
'''

# 用户名密码认证(私密代理/独享代理)
username = "772887864"
password = "bc9k2sms"

proxies = {
    "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {'user': username, 'pwd': password, 'proxy': random.choice(proxy_ip)},
    # "https": "https://%(user)s:%(pwd)s@%(proxy)s/" % {'user': username, 'pwd': password, 'proxy': random.choice(proxy_ip)}
}
headers = {
    'User-Agent': UserAgent().random
}

r = requests.get(page_url, proxies=proxies, headers=headers)
print(r.status_code)  # 获取Response的返回码

if r.status_code == 200:
    r.enconding = "utf-8"  # 设置返回内容的编码
    print(r.text)  # 获取页面内容
