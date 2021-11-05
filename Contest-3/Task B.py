def f(m):
    output = 1
    for i in range(1, m + 1):
        output *= i
    return output


def max_element(arr):
    arr += ' '
    output = []
    i = 0
    while i < len(arr) - 1:
        current = arr[i]
        j = 0
        while arr[i] == current and i < len(arr) - 1:
            i += 1
            j += 1
        output.append(j)
    return output


N = int(input())
names, res = [], 0
for n in range(N):
    names.append(input()[0])
names.sort()

for element in max_element(names):
    if element > 2:
        res += f(element // 2) / (f(2) * f(element // 2 - 2)) + f(element // 2 + element % 2) / (f(2) * f(element // 2 + element % 2 - 2))
print(int(res))
