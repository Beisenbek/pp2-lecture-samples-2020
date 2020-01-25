a = 179 ** 10
s = str(a) + str(a) + str(a) + str(a)
b = long(s) ** (1.0/10)
print(b)