class myObj:
  name = "John"

class myObj2(myObj):
  surname = "Smith"

y = myObj2()

print(y.name)


x = isinstance(y, myObj)

print(x)
