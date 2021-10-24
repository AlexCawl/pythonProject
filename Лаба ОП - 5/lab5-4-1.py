def triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Треугольник не существует"
    elif a + b + c - max(a, b, c) <= max(a, b, c):
        return "Треугольник не существует"
    elif a == b == c:
        return "Треугольник равносторонний"
    elif a == b or b == c or c == a:
        return "Треугольник равнобедренный"
    else:
        return "Треугольник общего вида"


side1, side2, side3 = list(map(float, input().strip().split()))
print(triangle(side1, side2, side3))