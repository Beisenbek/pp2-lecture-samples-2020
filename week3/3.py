import math

def f(x):
    if x == 1: 
        return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    
    return True

res = list(range(1, 1001))
res2 = [i for i in res if f(i)]
print(res2)

