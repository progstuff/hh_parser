#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Юзверь
#
# Created:     05.11.2021
# Copyright:   (c) Юзверь 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import urllib.request

def main():



    pass

if __name__ == '__main__':
    main()


URL = "https://tver.hh.ru/search/vacancy?clusters=true&ored_clusters=true&enable_snippets=true&salary=&text=developer&page=2"
headers = {

    'Host': 'tver.hh.ru',
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://tver.hh.ru/search/vacancy?clusters=true&ored_clusters=true&enable_snippets=true&salary=&text=developer',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'
}

r = urllib.request.urlopen(url = URL)

pageText = r.text

keyWord = 'vacancy-serp__vacancy-title'
t = pageText
i1 = 0
i2 = 0
n = len(pageText)
cnt = 0
while(i1 > -1):
    n = len(t)
    i1 = t.find(keyWord)
    cnt = cnt + 1

    if(i1 > -1):
        i2 = i2 + i1
        t = pageText[i2+1:n-1]
        print(i2, cnt)

with open('t.txt', 'w') as f:
    f.write(pageText)