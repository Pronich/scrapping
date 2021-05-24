from bs4 import BeautifulSoup
import requests
from pprint import pprint
from datetime import date

def get_post(keywords, link):
    response = requests.get(link).text
    soup = BeautifulSoup(response, features="html.parser")
    articles = soup.find_all('article', class_='post')
    for post in articles:
        for keyword in keywords:
            if post.text.lower().find(keyword) != -1:
                art_title = post.find('a', class_='post__title_link').text
                art_href = post.find('a', class_='post__title_link').attrs.get('href')
                post_time = post.find('span', class_='post__time').text
                if post_time.find('сегодня') != -1:
                    post_time = str(date.today()) + ' ' + post_time.split(' ')[2]
                pprint('<' + post_time + '> - <' + art_title + '> - <' + art_href + '>')
                break
