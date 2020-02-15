import re

text1 = "admin@kbtu.kz"
text2 = "@kbtu.kz"
pattern = r"[a-z]+@[a-z]+\.[a-z]{2}"

res1 = re.match(pattern,text1)
res2 = re.match(pattern,text2)

print(res1)
print(res2)
