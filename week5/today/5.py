import re

text = "v"
pattern = r"a*"

res = re.match(pattern, text)
print(res)
