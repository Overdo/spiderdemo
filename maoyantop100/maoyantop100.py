# encoding:utf-8
import requests
import timeit
import re
from requests.exceptions import RequestException
import json
from multiprocessing import Pool, Lock, Queue
import os

def get_one_page(url):
    header = {
        'User-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
    }
    try:
        response = requests.get(url, headers=header)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except RequestException:
        return None


def parse_one_page(html):
    partern = re.compile('<dd>.*?board-index.*?">(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?"integer">(.*?)</i>.*?'
                         + '"fraction">(.*?)</i>', re.S)
    items = re.findall(partern, html)
    for item in items:
        yield {
            'rank': item[0],
            'img': item[1],
            'name': item[2],
            'star': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }


def write_to_file(content):

    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        write_to_file(item)




if __name__ == '__main__':

    for i in range(10):
        main(i * 10)
    # print(timeit.timeit(main, number=1))


















