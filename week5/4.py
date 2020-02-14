import re

pattern = r"\n{1}(?P<raw_count>.*)\n{1}(?P<price>.*)\n{1}(Стоимость)\n{1}(?P<price2>.*)"

file1 = open('raw.data', 'r') 
text = file1.read()

#print(text)

#print(re.match(pattern, text).span())
print(re.findall(pattern, text))
#print(re.findall(pattern, text))