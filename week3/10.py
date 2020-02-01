def fib(max):
    a = 0
    b = 1     
    while a < max:
        yield a
        c = a + b          
        a = b
        b = c

for i in fib(100):
    print(i)


