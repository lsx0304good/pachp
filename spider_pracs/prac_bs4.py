from bs4 import BeautifulSoup
import requests
from requests import Response
from fake_useragent import UserAgent

data = 'https://movie.douban.com/top250?start=0&filter='
# detail_page = 'https://movie.douban.com/subject/{movie_id}/'.format(movie_id=movie_id)

headers = {"User-Agent": UserAgent().random}


def get_detailed_url(home_url):
    resp: Response = requests.get(url=home_url, headers=headers)
    if resp.status_code == 200:
        html = resp.text
        soup = BeautifulSoup(html, 'lxml')
        lis = soup.find('ol', class_='grid_view').find_all("li")
        detailed_urls = []

        for li in lis:
            detailed_url = li.find("a").attrs.get("href")
            # print(detailed_url)
            detailed_urls.append(detailed_url)
    return detailed_urls



def parse_detailed_url(url):
    resp: Response = requests.get(url=url, headers=headers)
    if resp.status_code == 200:
        html = resp.text
        soup = BeautifulSoup(html, 'lxml')

        movie_name = list(soup.find('div', id='content').find('h1').stripped_strings)[0]

        movie_director = list(soup.find('div', id='info').find('span').find('span', class_='attrs').stripped_strings)
        movie_director = "".join(movie_director)

        movie_writer = list(soup.find('div', id='info').find_all('span')[3].find('span', class_='attrs').stripped_strings)
        movie_writer = "".join(movie_writer)

        # save()




def main():
    home_url = 'https://movie.douban.com/top250?start={}&filter='
    for i in range(0, 226, 25):
        home_url = home_url.format(i)
        detailed_urls = get_detailed_url(home_url)
        for url in detailed_urls:
            parse_detailed_url(url)


if __name__ == '__main__':
    main()
