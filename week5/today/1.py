import re

text = "test string:  21"
pattern = r"^.*s.*$"

res = re.match(pattern, text)
print(res)
