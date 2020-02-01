listx = [0, 1]

def f(max):
    n = len(listx)
    x = listx[n - 1] + listx[n - 2]
    if(x <= max): 
        listx.append(x)
        f(max)

f(100)
print(listx)
