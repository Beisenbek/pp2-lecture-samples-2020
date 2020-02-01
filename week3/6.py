def f(max):
    res = []
    i = 0
    j = 1

    while(i <= max):
        k = i + j
        res.append(i)
        i = j
        j = k

    return res

l = f(1000)
print(l)
