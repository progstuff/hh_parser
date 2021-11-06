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

import requests

def main():
    pass

if __name__ == '__main__':
    main()

class Vacancy:

    def getVacancyData(self, vacancyText):
        i1 = vacancyText.find('?')
        if(vacancyText[0] == '"'):
            self.ref = vacancyText[1:i1]
        else:
            self.ref = vacancyText[0:i1]
        i1 = vacancyText.find('">')
        self.name = vacancyText[i1+2:len(vacancyText)]

    def getVacancyStr(self):
        return self.name + ';' + self.ref

class PageParser:
    def setPageText(self, pageText):
        self.elementIndexStart = []
        self.vacancyText = []
        self.pageText = pageText

    def findElements(self, keyWord):
        t = self.pageText
        i1 = 0
        i2 = 0
        n = len(self.pageText)
        cnt = 0

        while(i1 > -1):
            #n = len(t)
            i1 = t.find(keyWord)
            cnt = cnt + 1
            #print(i1)
            if(i1 > -1):
                i2 = i2 + i1 + len(keyWord)
                self.elementIndexStart.append(i2)

                t = self.pageText[i2+1:n-1]
                #print(i2, cnt)
        return [cnt]

    def findVacancyText(self):
        n = len(self.pageText)
        for i in range(0,len(self.elementIndexStart)):
            i1 = self.elementIndexStart[i]
            i2 = self.pageText[i1:n].find('</a>')
            self.vacancyText.append(self.pageText[i1:i1 + i2])

        i = 5

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


#searchQueryes = ['разработчик','Python','программист python','Android','Android developer','developer', 'unity', 'junior developer']
searchQueryes = ['unity', 'junior developer']
pageParser = PageParser()

for searchQuery in searchQueryes:
    currentPageIndex = 0
    gCnt = 0
    isError = False
    with open(searchQuery + '.txt', 'w') as f:
        while(not(isError)):

            vacancies = []
            URL = "https://tver.hh.ru/search/vacancy?clusters=true&ored_clusters=true&enable_snippets=true&salary=&text=" + searchQuery + "&page=" + str(currentPageIndex)
            r = requests.get(url = URL, headers = headers)
            if(r.status_code == 404):
                isError = True
            else:
                print("#############Current Page is - ", currentPageIndex, "#############")
                pageParser.setPageText(r.text)

                keyWord = '<a class="bloko-link" data-qa="vacancy-serp__vacancy-title" target="_blank" href="'
                cnt = pageParser.findElements(keyWord)
                pageParser.findVacancyText()

                for i in range(0,cnt[0]-1):
                    v = Vacancy()
                    v.getVacancyData(pageParser.vacancyText[i])
                    vacancies.append(v)
                    gCnt = gCnt + 1
                    f.write(str(gCnt) + ";" + v.getVacancyStr() + "\n")
                    print(searchQuery, gCnt, v.getVacancyStr())


                currentPageIndex = currentPageIndex + 1