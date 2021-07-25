import requests
from fake_useragent import UserAgent
from requests import Response
from lxml import etree
import os

headers = {
    "User-Agent": UserAgent().random,
}


def request():
    url = "https://www.huya.com/g/4079"
    resp: Response = requests.get(url=url, headers=headers)
    if resp.status_code == 200:
        print("successful")
        parse(resp.text)

    else:
        print("failed", resp.status_code)


def parse(data):
    html_etree = etree.HTML(data)
    pics = html_etree.xpath("//img[@class='pic']")

    for pic in pics:
        img_url = pic.xpath(".//@data-original")[0]
        img_url = img_url.split("?")[0]

        img_name = pic.xpath("./@alt")[0][:-3]

        image = requests.get(url=img_url, headers=headers)

        if not os.path.exists("streamers"):
            os.mkdir("streamers")

        with open("streamers/%s.jpg" % img_name, "wb") as f:
            f.write(image.content)


if __name__ == '__main__':
    request()
