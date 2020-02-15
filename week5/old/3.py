import re

pattern = r"(Стоимость)\n{1}(?P<price>.*)"

file1 = open('raw.data', 'r') 
text = file1.read()

#print(text)

#print(re.match(pattern, text).span())
print(re.findall(pattern, text))
#print(re.search(pattern, text).group("price"))
#print(re.findall(pattern, text))