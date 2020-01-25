from fractions import Fraction

sign = 1
sum = 0

for i in range(1,20,2):
    sum = sum + Fraction(sign * 4, i)
    sign = -sign

print(sum)
print(1.0 * sum.numerator / sum.denominator)