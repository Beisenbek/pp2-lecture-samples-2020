import re

pattern = r"(Стоимость)\n{1}(.*)"

file1 = open('raw.data', 'r') 
text = file1.read()

#print(text)

#print(re.match(pattern, text).span())
print(re.search(pattern, text).group(2))
#print(re.findall(pattern, text))