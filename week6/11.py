x = ('apple', 'banana', 'cherry')
r = x
y = id(x)
t = id(r)
z = hash(x)
print(y)
print(z)
print(t)
