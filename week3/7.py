def f(listx, max):
    n = len(listx)
    x = listx[n - 1] + listx[n - 2]
    if(x > max): return listx
    listx.append(x)
    return f(listx, max)

nums = [0, 1]
l = f(nums, 100)
print(l)
