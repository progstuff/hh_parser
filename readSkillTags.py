#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Юзверь
#
# Created:     06.11.2021
# Copyright:   (c) Юзверь 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import headHunterSearchParcer as hhParser
import os


def getUniqueElements(directoryName):
    files = os.listdir(directoryName)
    vacancies = []
    for f in files:
        with open(directoryName + "/" + f, 'r') as fdata:
            info = fdata.readlines()
            vacancies = [*vacancies, *info]

    k = 0
    nVacancies = vacancies.copy()
    ind1 = []
    for i in range(0, len(vacancies)):
        cnt = 0
        v1 = vacancies[i]
        ind2 = []
        for j in range(0, len(nVacancies)):
            if(j != i):
                v2 = nVacancies[j]
                if(v1 == v2):
                    nVacancies[j] = ''
                    ind2.append(j)
                    k = k + 1
        if(len(ind2) > 0):
            #ind2.append(i)
            ind1.append(ind2)

    j = 0
    for v in nVacancies:
        if(v == ''):
            j = j + 1

    nVacancies = [x for x in nVacancies if x != '']
    return nVacancies

def deleteVacancies(vacancies, listVacancies):
    nVacancies = vacancies.copy()
    for i in range(0, len(vacancies)):
        v1 = vacancies[i]
        for j in range(0, len(listVacancies)):
            v2 = listVacancies[j]
            if(v2 in v1):
                nVacancies[i] = ''
                break
    nVacancies = [x for x in nVacancies if x != '']
    return nVacancies

def main():

    inputDirectoryName ='headHunterVacancies'
    vacancies1 = getUniqueElements(inputDirectoryName)

    listVacancies = ['Курьер', 'курьер', 'Водитель','водитель','Комплектовщик', 'комплектовщик', 'технолог', 'Технолог']
    vacancies = deleteVacancies(vacancies1, listVacancies)

    tags = []
    with open('skillTags.txt','w') as f:
        for i in range(0, len(vacancies)):
            v = hhParser.VacancyDetailedInfo()
            v.getVacancyData(vacancies[i])
            print(i, v.getVacancyStr())
            r = v.loadVacancyPage()
            if(r.status_code == 200):
                parser = hhParser.SearchPageParser()
                parser.setPageText(r.text)
                keyValue = 'data-qa="bloko-tag__text">'
                parser.findElements(keyValue)
                parser.findSkillTags()
                for x in parser.skillTags:
                    f.write(x + '\n')
    pass

if __name__ == '__main__':
    main()

##inputDirectoryName ='headHunterVacancies'
##vacancies1 = getUniqueVacancies(inputDirectoryName)
##
##listVacancies = ['Курьер', 'курьер', 'Водитель','водитель','Комплектовщик', 'комплектовщик', 'технолог', 'Технолог']
##vacancies = deleteVacancies(vacancies1, listVacancies)

