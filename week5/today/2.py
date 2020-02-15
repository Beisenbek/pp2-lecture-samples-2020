import re

text = "test string:  21"
pattern = r"[abcdefghijklmnopqrstuvwxyz\s]*[:\s0123456789]*"

res = re.match(pattern, text)
print(res)
