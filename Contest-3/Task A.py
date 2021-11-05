N = int(input())
res = []
for n in range(N):
    a, b, c = list(map(int, input().split()))
    output = (a + b + c) // 2
    res.append(output)
for element in res:
    print(element)