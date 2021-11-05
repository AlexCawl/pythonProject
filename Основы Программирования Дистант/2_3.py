# №3
# Сформулируйте алгоритм возведения в целую степень целого числа.

x = int(input())
n = int(input())
result, i = 1, 0

while i < abs(n):
    result *= x
    i += 1

if n >= 0:
    print(result)
else:
    print(1 / result)