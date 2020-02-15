import re

file = open('raw.data', 'r') 
text = file.read()

pattern_text = r"(?P<name>.*)\n{1}(?P<count>.*)x(?P<price>.*)\n{1}(?P<total1>.*)\n{1}(?P<title>Стоимость)\n{1}(?P<total2>.*)"
pattern = re.compile(pattern_text)

for m in re.finditer(pattern, text):
    print(m.group("name"), '=======', m.group("price"))