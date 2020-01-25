sign = 1
sum = 0

for i in range(1,20,2):
    sum = sum + (sign * 4.0) / i
    sign = -sign


print(sum)