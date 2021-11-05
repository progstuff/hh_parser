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

def main():
    pass

if __name__ == '__main__':
    main()

option = webdriver.ChromeOptions()
option.add_argument('headless')
browser = webdriver.Chrome(ChromeDriverManager().install(), options = option)

for i in range(10,15):
    URL = "https://tver.hh.ru/search/vacancy?clusters=true&ored_clusters=true&enable_snippets=true&salary=&text=developer&page="+str(i)

    browser.get(URL)

    with open('t' + str(i) + '.txt', 'w') as f:
        f.write(browser.page_source)

    print(i)
    #print(browser.page_source)