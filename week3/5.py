def f(max):
    i = 0
    j = 1
    while(i <= max):
        k = i + j
        print(i)
        i = j
        j = k

f(1000)
