import csv
Country=[]
DemocracyScore=[]
AgriculturalLand=[]
Exports=[]
GDPpercapita=[]
Imports=[]
IncomePerPerson=[]
Medianage=[]
Poverty=[]
Ratioofgirlstoboysinprimaryandsecondaryeducation=[]
Taxrevenue=[]

with open('Gapminder.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        Country.append(row[0])
        DemocracyScore.append(row[12])
        AgriculturalLand.append(row[6])
        Exports.append(row[14])
        GDPpercapita.append(row[17])
        Imports.append(row[21])
        IncomePerPerson.append(row[22])
        Medianage.append(row[32])
        Poverty.append(row[41])
        Ratioofgirlstoboysinprimaryandsecondaryeducation.append(row[42])
        Taxrevenue.append(row[46])

csvFile.close()

for j in range(1,len(Country)):
    country_name=Country[j]
    score=0
    count=1
    for i in range(len(Country)):
        if country_name==Country[i]:
            if DemocracyScore[i] != 'empty':
                score=score+int(DemocracyScore[i])
                count=count+1
    print("average Democracy score of ",country_name,"is",score/count)          


