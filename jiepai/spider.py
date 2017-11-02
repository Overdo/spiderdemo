# encoding:utf-8
from requests.exceptions import RequestException
import requests
import json
from urllib.parse import urlencode


def get_page_index(offset, keyword):
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': True,
        'count': 20,
        'cur_tab': 1
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
    print(url)
    try:
        html = requests.get(url)
        if html.status_code == 200:
            return html.text
        else:
            return None
    except RequestException:
        print("请求索引页出错了")
        return None


def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')


def get_page_detail(url):
    try:
        html = requests.get(url)
        if html.status_code == 200:
            return html.text
        else:
            return None
    except RequestException:
        print("请求详情页出错了")
        return None


def parse_page_detail(html):

    pass

def main():
    html = get_page_index(40, '美女')
    for url in parse_page_index(html):
        # html = get_page_detail(url)
        print(url)


if __name__ == '__main__':
    main()

















