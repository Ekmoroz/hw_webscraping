# import bs4
import requests
from bs4 import BeautifulSoup

url = 'https://habr.com/ru/all/'
req = requests.get(url)
text = req.text

# Вывести в консоль список подходящих статей в формате: <дата> - <заголовок> - <ссылка>.

# определяем список ключевых слов
KEYWORDS = {'дизайн', 'фото', 'web', 'python'}

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
    article_hubs = set([hub.find('span').text for hub in hubs])
    if KEYWORDS & article_hubs:
        print(f'{date} - {my_title} - {url_1}')




