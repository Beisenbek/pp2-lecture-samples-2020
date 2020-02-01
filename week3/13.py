class Fib:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1       
        return self
    
    def __next__(self):
        res = self.a
        if self.a > self.max: raise StopIteration   
        c = self.a + self.b
        self.a = self.b
        self.b = c
        return res

fib = Fib(100)

for i in fib:
    print(i)



