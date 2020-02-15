import re

text = "test string:  21"
pattern = r"[\w\s]*[:\s\d]*"

res = re.match(pattern, text)
print(res)
