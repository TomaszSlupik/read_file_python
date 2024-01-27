# Odczyt linia po linii
with open('data.txt', "r") as file:
    for line in file:
        print(line.strip())

print('---')

#  Każdej linii tego pliku znajduje się inna nazwa indeksu publikowanego przez
# Giełdę Papierów Wartościowych w Warszawie. Utwórz listę z nazwami indeksów
indexes = []
with open('indeksy.txt', "r", encoding='utf-8') as file:
    content = file.read()
    indexes.extend(content.replace('\n', ',').split(','))

print(indexes)

print('---')

with open ('plw_d.csv', "r") as file:
    content = list(file.read().split())
    print(content)

print('---')

# otrzymać słownik zawierający dwa klucze: 'Data' oraz 'Zamkniecie'. 
# Wartościami dla tych kluczy będą odpowiednio listy składające się z dat 
# oraz cen zamknięcia. Ceny zamknięcia przedstaw w postaci typu float.
listData = ['Data,Otwarcie,Najwyzszy,Najnizszy,Zamkniecie,Wolumen',
 '2020-03-02,305,324.5,283.5,310,64081',
 '2020-03-03,325.5,340.5,320,340.5,55496',
 '2020-03-04,324,340.5,315,330,36152',
 '2020-03-05,344,344,310,315,35992',
 '2020-03-06,306.5,307,291,305,32539',
 '2020-03-09,274,291,250,258,79402',
 '2020-03-10,278,284.5,256,264,35700',
 '2020-03-11,270,270,238.5,245,60445',
 '2020-03-12,218,228,196,197,94031',
 '2020-03-13,210,229,198.8,211,100412',
 '2020-03-16,205,248,197.8,240.5,50659',
 '2020-03-17,245,269,232.5,264,99480',
 '2020-03-18,264,280,251,270,70136',
 '2020-03-19,267,280,267,279.5,30732',
 '2020-03-20,297.5,307,280,280.5,43426',
 '2020-03-23,274,289,258,285,37098',
 '2020-03-24,305,309,296.5,309,31939',
 '2020-03-25,313,330,295,304,46724',
 '2020-03-26,300,309,295.5,300,27213',
 '2020-03-27,302,306.5,290,296,13466',
 '2020-03-30,299,300,287,300,10316',
 '2020-03-31,302.5,309,302,306.5,15698']

nameStrData = []
closeStrData = []
for nameData in listData[:1]:
    ele = nameData.split(',')
    nameStrData.append(ele[0])
    closeStrData.append(ele[4])

allData = []
allDataClose = []
for data in listData[1:]:
    elem = data.split(',')
    allData.append(elem[0])
    allDataClose.append(elem[4])

data_dict = {"".join(nameStrData): allData}
close_dict = {"".join(closeStrData): allDataClose}

data_dict.update(close_dict)

print(data_dict)

print('---')
# Znajdź największą wartość wolumenu w podanym miesiącu.
volumData = []
for volum in listData[1:]:
    ele = volum.split(',')
    volumData.append(ele[5])

print(f"Max Volume: {sorted(volumData)[0]}")

print('---')

# Znajdź dzień z największą wartością wolumenu w podanym miesiącu
maxVolum = []
for volum in listData:
    ele = volum.split(',')
    if ele[5] == 100412:
        maxVolum.append(ele)

print(f"Max Volume Date: {ele[0]}")

print('---')
# oblicza średnią energię wygenerowaną przez elektrownię wodną (trzecia kolumna, energia wyrażona w kWh)
energyData = ['date,time,energy',
'2023-03-31,00:00:00,123.4',
'2023-03-31,00:15:00,154.3',
'2023-03-31,00:30:00,189.5']

myEnergy = []
for energy in energyData[1:]:
    ele = energy.split(",")
    myEnergy.append(ele[2])

floatMyEnergy = [float(num) for num in myEnergy]
result = sum(floatMyEnergy) / len(floatMyEnergy)
print(f"Average energy generated: {result :.2f} kwh")
