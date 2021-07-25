import requests
from fake_useragent import UserAgent

''' POST

url = "https://fanyi.baidu.com/sug"
headers = {
    "User-Agent": UserAgent().random
}

data = {"kw": "apple"}

resp: requests.Response = requests.post(url, data=data)

assert resp.status_code == 200

print(resp.content)  # byte
print(resp.text)  # string
print(resp.json())  # json

'''


url = "https://tieba.baidu.com/f"

headers = {
    "User-Agent": UserAgent().random
}

params = {
    "ie": "utf-8",
    "kw": "Python",
    "pn": "50",
}

resp: requests.Response = requests.get(url, params=params)

assert resp.status_code == 200
print(resp.text)