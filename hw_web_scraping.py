# import bs4
import requests
from bs4 import BeautifulSoup


HEADERS = {'Cookie': '_ym_uid=1639148487334283574; _ym_d=1639149414; _ga=GA1.2.528119004.1639149415; _gid=GA1.2.512914915.1639149415; habr_web_home=ARTICLES_LIST_ALL; hl=ru; fl=ru; _ym_isad=2; __gads=ID=87f529752d2e0de1-221b467103cd00b7:T=1639149409:S=ALNI_MYKvHcaV4SWfZmCb3_wXDx2olu6kw',
          'Accept-Language': 'ru-RU,ru;q=0.9',
          'Sec-Fetch-Dest': 'document',
          'Sec-Fetch-Mode': 'navigate',
          'Sec-Fetch-Site': 'same-origin',
          'Sec-Fetch-User': '?1',
          'Cache-Control': 'max-age=0',
          'If-None-Match': 'W/"37433-+qZyNZhUgblOQJvD5vdmtE4BN6w"',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
          'sec-ch-ua-mobile': '?0'
}

# response = requests.get('https://habr.com/ru/all/', headers=HEADERS)

url = 'https://habr.com/ru/all/'
req = requests.get(url, headers=HEADERS)
text = req.text

# Вывести в консоль список подходящих статей в формате: <дата> - <заголовок> - <ссылка>.

# определяем список ключевых слов
KEYWORDS = {'дизайн', 'фото', 'web', 'python', 'Экология'}

soup = BeautifulSoup(text, features='html.parser')
# print(soup)

articles = soup.find_all('article')
for article in articles:
    # print(article)
    title = article.find('h2')
    my_title = title.text
    # print(title.text)     # заголовок
    tag_a = article.find('a')
    # print(tag_a.attrs['href'])
    url_1 = 'https://habr.com/ru/all/' + tag_a.attrs['href']
    # print(url_1)    # ссылка
    time = article.find('time')
    # print(time)
    date = time.attrs['title']
    # print(date)    # дата

    hubs = article.find_all('a', class_='tm-article-snippet__hubs-item-link')
    # print(hubs)
    article_hubs = set([hub.find('span').text for hub in hubs])
    # print(article_hubs)
    if KEYWORDS & article_hubs:
        print(f'{date} - {my_title} - {url_1}')




