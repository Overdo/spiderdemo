import random
import time
import requests
import re

'''
爬内涵吧的脑筋急转弯
'''

user_agent = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT6.1; Trident/5.0'
headers = {'User-Agent': user_agent}

all_list = []

for i in range(2,130):
    time.sleep(random.randrange(1,2))
    page_num = i
    url = 'http://www.neihanpa.com/njjzw/index_' + str(page_num) + '.html'

    response = requests.get(url, headers=headers,)

    if response.status_code == 200:
        content = response.text.encode(response.encoding).decode()
        parttern = re.compile("class=\"title\"\stitle=\"(.*?)\">.*?</a></h3>.*?class=\"desc\">\s+(.*?)</div>",re.S)
        itemlist = parttern.findall(content)
        print(itemlist)

        all_list.extend(itemlist)

f = open('njjzw.txt','a', encoding="utf-8")
for item in all_list:
    f.write(str(item))
    f.write('\n')
f.close()



