import re

file1 = open('raw.data', 'r') 
text = file1.read()

pattern = re.compile(r"\n{1}(?P<name>.*)\n{1}(?P<raw_count>.*)\n{1}(?P<price>.*)\n{1}(Стоимость)\n{1}(?P<price2>.*)")

for m in re.finditer(pattern, text):
    print(m.group("name"), '=======', m.group("price"))