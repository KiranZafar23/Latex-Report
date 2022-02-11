def fetchIndices(list, columnInex, searchItem):
    row = 1
    lenght = len(list)
    listRowIndices = []
    for i in range(0,lenght):
        if searchItem == list[i][columnInex]:
            listRowIndices.append(i)
    return listRowIndices 

def fetchData(data, columnIndex, lisRowIndices):
    listDataValues = []
    for i in lisRowIndices:
        dat = data[i][columnIndex]
        listDataValues += [dat]
    return listDataValues    


import csv
with open('Gapminder.csv', 'r') as myFile:
    data = list(csv.reader(myFile, delimiter=','))


country_name = input("enter country name:  ")
result = fetchIndices(data, 0, country_name)
print(result)
# name of attributes
# agricultural land = 6
# DemocracyScore = 12
# Exports = 14
# GDPpercapita = 17
# Imports = 21
# IncomePerPerson = 22
# Medianage = 32
# Poverty = 41
# Ratioofgirlstoboysinprimaryandsecondaryeducation = 42
#Taxrevenue = 46
attribute = [6,12,14,17,21,22,32,41,42,46]
for k in attribute:
    result1 = fetchData(data, k , result)
    print(result1)
        