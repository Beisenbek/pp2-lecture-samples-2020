
#bin, znm, kassa, check,
#vremya, address
import json

class Item:
    def __init__(self, name, cena, kolvo,stoimost):
        self.name = name
        self.cena = cena
        self.kolvo = kolvo
        self.stoimost = stoimost
    def appendHeader(self, bin, znm, kassa, check):
        self.bin = bin
        self.znm = znm
        self.kassa = kassa
        self.check = check

    def appendFooter(self, vremya, address):
        self.vremya = vremya
        self.address = address

file1 = open('raw.data', 'r') 
Lines = file1.readlines() 


headers = ["БИН", "Касса", "Чек"]
lines = []
items = []

dic = {}

for rawLine in Lines: 
    lines.append(rawLine)

for i in range(0, len(lines), 1): 
    for header in headers:
        headerPos = lines[i].find(header)
        if headerPos != -1:
                headerValue = lines[i][headerPos + len(header):].strip()
                dic[header] = headerValue
                #print(headerValue)
    
    timePos = lines[i].find("Время")
    if timePos != -1:
        address = lines[i + 1].strip()
        time = lines[i][timePos + 6:].strip()
        #print(time)
        #print(address)
        dic["Время"] = time
        dic["Адрес"] = address

    ZNMPos = lines[i].find("ЗНМ")
    if ZNMPos != -1:
        ZNMValue = lines[i][ZNMPos + 4:].strip()
        #print(ZNMValue)
        dic["ЗНМ"] = ZNMValue


    prodazhaPos = lines[i].find("ПРОДАЖА")

    if prodazhaPos != -1:
        j = i + 1
        while True :
            itogoPos = lines[j].find("ИТОГО")
            if itogoPos != -1: break

            name = lines[j + 1].strip()
            stoimost = lines[j + 5].strip()
            x = lines[j + 2].split('x')
            
            if len(x) != 2: break;
            
            kolvo = x[0].strip()
            cena =  x[1].strip()

            #print(name + "\n" + cena + "\n" + kolvo + "\n" + stoimost)

            item = Item(name,cena,kolvo,stoimost)
            items.append(item)

            j = j + 6


def dumper(obj):
    try:
        return obj.toJSON()
    except:
        return obj.__dict__

for i in range(0, len(items), 1):
    items[i].appendHeader(dic["БИН"],dic["ЗНМ"], dic["Касса"],dic["Чек"])    
    items[i].appendFooter(dic["Адрес"],dic["Время"])

titles = ["БИН","ЗНМ","Касса","Чек","Наименование товара","Цена за единиц","Кол-во", "Сумма", "Дата и Время","Адрес"]
iterable = []
iterable.append(titles)

for i in range(0, len(items), 1):
    iterable.append([items[i].bin,items[i].znm,items[i].kassa,items[i].check,items[i].name,items[i].cena,items[i].stoimost,items[i].kolvo,items[i].vremya,items[i].address])

import csv
with open('file.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(iterable)

