import re

text = "av"
pattern = r"a+"

res = re.match(pattern, text)
print(res)
