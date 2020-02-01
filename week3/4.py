import math

def f(x):
    if x == 1: return False
    i = 2
    res = True
    while i * i <= x:
        if x % i == 0: 
            res = False
            break
        i = i + 1

    return res

res = list(range(1, 1001))
res2 = [i for i in res if f(i)]
print(res2)

