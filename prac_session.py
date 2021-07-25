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
    'loginName': '18510170590',
    'password': 'lisixiang945',
}

session = requests.Session()

login_resp: Response = session.post(url=login_url, data=login_data, headers=headers)
if login_resp.status_code == 200:
    print("login succeed")

shelf_url = "https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919"
shelf_resp: Response = session.get(shelf_url, headers=headers)
print(shelf_resp.json())
