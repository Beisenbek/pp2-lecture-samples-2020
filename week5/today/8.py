import re

text1 = "hello!"
text2 = "hi!"
text3 = "hola!"

pattern = r"[hellohi]"

res1 = re.match(pattern, text1)
res2 = re.match(pattern, text2)
res3 = re.match(pattern, text3)

print(res1)
print(res2)
print(res3)
