import re

file = open('raw.data', 'r') 

pattern = r"(?P<title>Порядковый номер чека)\s+(?P<number>.*)\s+"

text = file.read()

print(re.search(pattern, text).group("number"))