def f(listx, max):
    n = len(listx)
    x = listx[n - 1] + listx[n - 2]
    if(x > max): return listx
    return f(listx + [x], max)

nums = [0, 1]
l = f(nums, 1000)
print(l)
