class MyClass:
    #x = 5
    def __init__(self):
        self.x = 7


p1 = MyClass()
print(p1.x)
print(getattr(p1, 'x'))