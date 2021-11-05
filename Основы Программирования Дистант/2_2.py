# №2
# Как переделать программу с предыдущего слайда таким образом, чтобы она работала и для отрицательных чисел?
# Вычисление r = y % x, d = y // x

y = int(input())
x = int(input())
r = y
d = 0

if y > 0 and x > 0:
    while r >= x:
        r -= x
        d += 1
elif y < 0 and x > 0:
    while r + x <= x:
        r += x
        d -= 1
elif y > 0 and x < 0:
    while r + x >= x:
        r += x
        d -= 1

print(str(y) + " % "  + str(x) + " = " + str(r))
print(str(y) + " // " + str(x) + " = " + str(d))