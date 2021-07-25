from lxml import etree
import requests
from fake_useragent import UserAgent
from requests import Response

headers = {
    "User-Agent": UserAgent().random
}

url = 'https://category.dangdang.com/pg{page}-cp01.54.00.00.00.00.html'

def get_url(url):
    res: Response = requests.get(url, headers=headers)
    parse_url(res.text)

def parse_url(html):
    myetree = etree.HTML(html)
    li_list = myetree.xpath("//ul[@class='bigimg']/li")

    for li in li_list:
        book_name = li.xpath('./p[@class="name"]/a/text()')[0]
        book_price = li.xpath('./p[@class="price"]/span[@class="search_now_price"]/text()')[0]
        book_img = "http:" + (li.xpath('./a/img/@data-original')[0] if li.xpath('./a/img/@data-original') else li.xpath('./a/img/@src')[0])
        book_info.append([book_name, book_price, book_img])


if __name__ == '__main__':
    book_info = []
    for page in range(1, 6):
        get_url(url.format(page=page))
    with open("dangdang.txt", 'a', encoding='utf-8') as f:
        for book in book_info:
            f.write("book name: " + str(book[0]) + "\n" + "book price: " + str(book[1]) + "\n" + "book img url: " + str(book[2]) + "\n\n")
            f.flush()

