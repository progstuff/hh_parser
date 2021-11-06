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

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def main():
    pass

if __name__ == '__main__':
    main()

option = webdriver.ChromeOptions()
option.add_argument('headless')
caps = DesiredCapabilities().CHROME
#caps["pageLoadStrategy"] = "normal"  #  complete
caps["pageLoadStrategy"] = "eager"  #  complete
#caps["pageLoadStrategy"] = "none"  #  complete
browser = webdriver.Chrome(ChromeDriverManager().install(), options = option, desired_capabilities=caps)

startPageIndex = 1
endPageIndex = 1
searchQuery = 'developer'

print("start download pages")
for currentPageIndex in range(startPageIndex, endPageIndex + 1):
    URL = "https://tver.hh.ru/search/vacancy?clusters=true&ored_clusters=true&enable_snippets=true&salary=&text=" + searchQuery + "&page=" + str(currentPageIndex)

    browser.get(URL)

    with open('t' + str(currentPageIndex) + '.txt', 'w') as f:
        f.write(browser.page_source)

    print(currentPageIndex)
    #print(browser.page_source)

    keyWord = '"company":'
    t = browser.page_source
    i1 = 0
    i2 = 0
    n = len(browser.page_source)
    cnt = 0
    while(i1 > -1):
        i1 = t.find(keyWord)
        cnt = cnt + 1

        if(i1 > -1):
            i2 = i2 + i1
            t = browser.page_source[i2+1:n-1]
            #print(i2, cnt)
