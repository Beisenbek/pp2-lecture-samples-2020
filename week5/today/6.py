import re

text = "aaaa"
pattern = r"a{3}"

res = re.match(pattern, text)
print(res)
