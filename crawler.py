import requests
import time
import re
from bs4 import BeautifulSoup

global count
count = 0


def split_text(text):
    text = re.sub('([。！？\?])([^”’])', r"\1\n\2", text)
    text = re.sub('([。！？\?][”’])([^，。！？\?])', r'\1\n\2', text)
    text = text.rstrip()
    return text.split("\n")


def get_text(url):
    global count
    try:
        src = requests.get(url).content
        bs_src = BeautifulSoup(src, features="lxml")
        nodes = bs_src.find_all('p')
        text = ''
        for p in nodes:
            text = p.get_text()
            words = split_text(text)
            for word in words:
                if word.strip() == '':
                    continue
                save(f'text\\content{count}.txt', word)
                print(count)
                count += 1
                if count >= 300:
                    return
    except requests.RequestException:
        return None


def get_urls(root_url):
    src = requests.get(root_url, verify=False).content
    bs_src = BeautifulSoup(src, "lxml")
    hrefs = bs_src.find_all('a')
    links = []
    for a in hrefs:
        if a.get('href'):
            if 'http' in a.get('href'):
                link = a.get('href')
            else:
                link = root_url + a.get('href')
            if link.strip() != "":
                links.append(link)
    return links


def save(filename, contents):
    fh = open(filename, 'w', encoding='utf-8')
    fh.write(contents)
    fh.close()


def Crawler():
    root_url = 'https://www.zj.gov.cn/'
    links = get_urls(root_url)
    for link in links:
        get_text(link)
        if count >= 300:
            break
