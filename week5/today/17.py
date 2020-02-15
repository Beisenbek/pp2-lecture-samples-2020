import re

file = open('raw.data', 'r') 
text = file.read()

pattern = r"(?P<name>.*)\n{1}(?P<count>.*)x(?P<price>.*)\n{1}(?P<total1>.*)\n{1}(?P<title>Стоимость)\n{1}(?P<total2>.*)"

print(re.findall(pattern, text))