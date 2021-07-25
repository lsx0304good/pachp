import json
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

    new_houses = []
    for each in houses:
        sublist = []
        sublist.append(each[0].lstrip("\n").strip())
        type_area_list = re.split(r"\s+(&nbsp;){4,}", each[1].lstrip())
        sublist.append(type_area_list[0])
        sublist.append(type_area_list[2].rstrip().rstrip("\n"))
        sublist.append(each[2])
        new_houses.append(sublist)
        print(sublist)

    save_data(new_houses)



def save_data(result_list):
    with open("house1.json", "w", encoding='utf-8') as f:
        json.dump(result_list, f, ensure_ascii=False)



def main():
    url = 'https://bj.58.com/chuzu/'
    get_data(url)


if __name__ == '__main__':
    main()
