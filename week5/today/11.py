import re

text1 = "admin@kbtu.kz"
pattern = r"(?P<login>[a-z]+)@(?P<domain>[a-z]+)\.(?P<country>[a-z]{2})"

res1 = re.match(pattern,text1)

print(res1.group("login"))
print(res1.group("country"))
print(res1.group("domain"))
