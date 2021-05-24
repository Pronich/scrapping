import configparser
from habr_scrapping import get_post

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read("settings.ini")
    keywords = config['KEYWORDS']['KEYWORDS'].split(',')
    get_post(keywords, 'https://habr.com/ru/all/')