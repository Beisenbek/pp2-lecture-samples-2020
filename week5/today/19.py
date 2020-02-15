import re

file = open('raw.data', 'r') 
text = file.read()

BINPattern = r"\nБИН(?P<BIN>.*)"
KASSAPattern = r"\nКасса(?P<KASSA>.*)"
CHECKPattern = r"\nЧек(?P<CHECK>.*)"
TIME_ADDRESSPattern = r"\nВремя:(?P<TIME>.*)\n(?P<ADDRESS>.*)"
ZNMPattern = r"\nЗНМ:(?P<ZNM>.*)"
item_pattern_text = r"(?P<name>.*)\n{1}(?P<count>.*)x(?P<price>.*)\n{1}(?P<total1>.*)\n{1}(?P<title>Стоимость)\n{1}(?P<total2>.*)"
item_pattern = re.compile(item_pattern_text)

BINText = re.search(BINPattern, text).group("BIN").strip()
KASSAText = re.search(KASSAPattern, text).group("KASSA").strip()
CHECKText = re.search(CHECKPattern, text).group("CHECK").strip()
ADDRESSText = re.search(TIME_ADDRESSPattern, text).group("ADDRESS").strip()
TIMEText = re.search(TIME_ADDRESSPattern, text).group("TIME").strip()
ZNMText = re.search(ZNMPattern, text).group("ZNM").strip()

items = [["БИН","ЗНМ","Касса","Чек","Наименование товара","Цена за единиц","Кол-во", "Сумма", "Дата и Время","Адрес"]]

for m in re.finditer(item_pattern, text):
    items.append([BINText, ZNMText, KASSAText,CHECKText,m.group("name").strip(), m.group("price").strip(), m.group("count").strip(), m.group("total1").strip(), TIMEText, ADDRESSText])

import csv
with open('file.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(items)