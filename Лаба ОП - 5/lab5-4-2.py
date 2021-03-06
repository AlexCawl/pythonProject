# Дополнительные требования:
# Нахождение корней при A = 0, то есть решение линейного уравнения
def output(A, B, C, counter, roots):
    print(f"Уравнение\n({'%.5f' % A})*X^2+({'%.5f' % B})*X+({'%.5f' % C})=0")
    print(f"Количество корней: {counter}")
    if len(roots) > 0:
        for root in roots:
            print('%.5f' % root)


def equation(A, B, C):
    if A != 0:
        D = B ** 2 - 4 * A * C
        if D < 0:
            output(A, B, C, 0, [])
        elif D == 0:
            output(A, B, C, 1, [((-1) * B) / (2 * A)])
        else:
            output(A, B, C, 2, [((-1) * B - D ** 0.5) / (2 * A), ((-1) * B + D ** 0.5) / (2 * A)])
    elif B == 0:
        print("Бесконечное множество решений")
    else:
        output(A, B, C, 1, [((-1)*C)/B])


a, b, c = list(map(float, input().split()))
equation(a, b, c)