# 需求：爬17k小说网 登陆之后的内容
import json

import requests
from requests import Response
from fake_useragent import UserAgent

# simulate login
# request url

login_url = "https://passport.17k.com/ck/user/login"
headers = {
    'User-Agent': UserAgent().random,
}

# setup username and pwd
login_data = {
    'loginName': '',
    'password': '',
}

# send POST request
resp: Response = requests.post(url=login_url, data=login_data, headers=headers)
if resp.status_code == 200:
    print(resp.json())

# my shelf
shelf_url = "https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919"
cookies = resp.cookies

shelf_resp: Response = requests.get(shelf_url, headers=headers, cookies=cookies)

if shelf_resp.status_code == 200:
    # print(shelf_resp.text)
    print(shelf_resp.json())

