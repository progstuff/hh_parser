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

import headHunterSearchParcer
import os

def main():
    pass

if __name__ == '__main__':
    main()


def getUniqueVacancies(directoryName):
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


##directoryName ='headHunterVacancies'
##vacancies = getUniqueVacancies(directoryName)
parser = HeadHunterParser()

