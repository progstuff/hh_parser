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

from operator import itemgetter

def getUniqueElements(fileName):
    elements = []
    with open(fileName, 'r') as fdata:
        info = fdata.readlines()
        elements = [*elements, *info]

    k = 0
    nElements = []
    for i in range(0, len(elements)):
        v1 = elements[i]
        isAdded = False

        for j in range(0, len(nElements)):
            v2 = nElements[j]
            if(v1 == v2):
                isAdded = True
                break
        if(not(isAdded)):
            nElements.append(v1)

        if(i%1000 == 0):
            print(str(i/len(elements)*100))

    return [nElements,elements]

def main():
    pass

if __name__ == '__main__':
    main()

tags = getUniqueElements('skillTags.txt')
allTags = tags[1]
uniqueTags = tags[0]
result = []
for i in range(0,len(uniqueTags)):
    zn = [uniqueTags[i], 0]
    for j in range(0, len(allTags)):
        if(uniqueTags[i] == allTags[j]):
            zn[1] = zn[1] + 1
    result.append(zn)
    if(i%100 == 0):
        print(i / len(uniqueTags)*100)

sorted_result = sorted(result, key=itemgetter(1), reverse=True)

with open('popularTags.txt','w') as f:
    for x in sorted_result:
        vacancy = x[0]
        f.write(vacancy[0:len(vacancy)-1] + ';' + str(x[1]) + '\n')


