import requests
from bs4 import BeautifulSoup


def get_text(url):
    src = requests.get(url).content
    # print(page_source)
    bs_src = BeautifulSoup(src)
    report_text = bs_src.find_all('p')
    text = ''
    for p in report_text:
        text += p.get_text()
        text += '\n'
    return text


def get_urls(root_url):
    src = requests.get(root_url).content
    bs_src = BeautifulSoup(src)
    hrefs = bs_src.find_all('a')
    links = []
    for a in hrefs:
        if a.get('href'):
            if 'http' in a.get('href'):
                link = a.get('href')
            else:
                link = root_url + '/' + a.get('href')
            if link.strip():
                links.append(link)
    return links


def save(filename, contents):
    fh = open(filename, 'w', encoding='utf-8')
    fh.write(contents)
    fh.close()


if __name__ == '__main__':
    url = 'https://www.zj.gov.cn/'
    links = get_urls(url)
    i = 0
    for link in links:
        text = get_text(link)
        if text:
            save(f'.\\text\\content{i}.txt', text)
            i += 1
            print(i)
        if i >= 100:
            break
