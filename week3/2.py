def f(x):
    if x % 2 == 0:
         return False
    return True

res = list(range(1, 1001))
res2 = [i for i in res if f(i)]
print(res2)

