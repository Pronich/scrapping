from bs4 import BeautifulSoup
import requests
from pprint import pprint
from datetime import date

def get_data(link):
    response = requests.get(link).text
    soup = BeautifulSoup(response, features="html.parser")
    return soup

def get_href(post):
    return post.find('a', class_='post__title_link').attrs.get('href')

def get_post(keywords, link):
    soup = get_data(link)
    articles = soup.find_all('article', class_='post')
    for post in articles:
        art_href = get_href(post)
        main_post = get_data(art_href).find('article', class_='post')
        for keyword in keywords:
            if main_post.text.lower().find(keyword) != -1:
                art_title = post.find('a', class_='post__title_link').text
                post_time = post.find('span', class_='post__time').text
                if post_time.find('сегодня') != -1:
                    post_time = str(date.today()) + ' ' + post_time.split(' ')[2]
                pprint('<' + post_time + '> - <' + art_title + '> - <' + art_href + '>')
                break
