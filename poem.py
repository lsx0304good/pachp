import csv

import requests
from fake_useragent import UserAgent
from requests import Response
from lxml import etree

url = "https://so.gushiwen.cn/shiwens/"
headers = {
    "User-Agent": UserAgent().random
}


def get_data():
    resp = requests.get(url=url, headers=headers)
    if resp.status_code == 200:
        print("successful")
        parse_data(resp.text)
    else:
        raise Exception("failed")


def parse_data(data):
    print("yes")
    root = etree.HTML(data)
    divs = root.xpath("//div[@class='sons']")
    result_list = []

    for div in divs:
        poem_name = div.xpath(".//b/text()")
        if poem_name:
            poem_name = poem_name[0]
        else:
            poem_name = ""
        print(poem_name)

        poem_author = "".join(div.xpath(".//p[@class='source']/a/text()"))
        print(poem_author)

        plong = "".join(div.xpath(".//div[@class='contson']/p/text()"))
        pshort = "".join(div.xpath(".//div[@class='contson']/text()"))
        poem_content = plong if plong else pshort

        print(poem_content)

        result_list.append([poem_name, poem_author, poem_content])

    save_data(result_list)


def save_data(result_list):
    with open("poems.csv", "w", encoding='utf-8') as f:
        for sublist in result_list:
            writer = csv.writer(f)
            writer.writerow(sublist)


if __name__ == '__main__':
    get_data()
