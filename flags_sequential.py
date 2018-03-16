import os
import time

import requests
from requests_html import HTMLSession

session = HTMLSession()
r = session.get('http://flagpedia.net/')
images = r.html.find('div > a > img')
flag_images = ('http:' + img.attrs['src'] for img in images)

FOLDER = 'images'


def download_one(url):
    resp = requests.get(url)
    name = url.split('/')[-1]
    save_img(resp.content, name)
    return name


def show(name):
    print(name, end=' ')


def save_img(content, name):
    path = os.path.join(FOLDER, name)
    with open(path, 'wb') as img:
        img.write(content)
        show(name)


def download_many(url_list):
    for url in url_list:
        download_one(url)


def main():
    start = time.time()
    download_many(flag_images)
    end = time.time()
    elapsed = round(end - start, 4)
    print(elapsed)


if __name__ == '__main__':
    main()
