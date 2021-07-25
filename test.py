# from urllib.parse import urlencode
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from http.client import HTTPResponse  # 响应

from fake_useragent import UserAgent

#
# url = "http://www.mobiletrain.org/"
# response: HTTPResponse = req.urlopen(url)
#
# if response.code == 200:
#     print("请求成功")
#     r1 = response.read()
#     content = r1.decode("utf-8")
#     print(content)
# else:
#     print("请求失败，原因：", response.code)


url = "https://fanyi.baidu.com/sug"

headers = {
    "User-Agent": UserAgent().random
}


def translate(kw):
    data = {
        "kw": kw
    }

    req = Request(url, data=urlencode(data).encode("utf-8"), headers=headers)
    resp: HTTPResponse = urlopen(req)

    if resp.getcode() == 200:
        print("succeed")

        result = resp.read()
        # print(result)

        result1 = result.decode("utf-8")
        # print(result1)

        result2 = json.loads(result1)
        # print(result2)

        for content in result2['data']:
            print(content)

    else:
        print("failed")


if __name__ == '__main__':
    translate("friend")

# ua: UserAgent = UserAgent()
# print(ua.random)
