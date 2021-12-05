def div(a, b):
    if b == 0:
        return 'Не определено'
    elif a >= b:
        return 1 + div(a - b, b)
    else:
        return 0


A, B = list(map(int, input().split()))
print(f"div({A}, {B}) = {div(A, B)}")