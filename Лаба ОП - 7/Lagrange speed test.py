import time


def P(n, x):
    if n == 0:
        return 1.0
    elif n == 1:
        return x
    else:
        return (x * ((2 * n + 1) / (n + 1))) * P(n - 1, x) - ((n) / (n + 1)) * P(n - 2, x)


def P_smart(n, x, cache):
    if (n, x) in cache:
        return cache[(n, x)]

    if n == 0:
        cache.update({(n, x): 1.0})
    elif n == 1:
        cache.update({(n, x): x})
    else:
        cache.update({(n, x): (x*((2*n+1) / (n+1))) * P_smart(n - 1, x, cache) - (n/(n+1)) * P_smart(n - 2, x, cache)})
    return cache[(n, x)]


def P_no_recursia(n, x):
    res = [1, x]
    for k in range(2, n + 1):
        res.append((x * ((2 * k + 1) / (k + 1))) * res[k - 1] - (k / (k + 1)) * res[k - 2])
    return res[n]


N = 30 #int(input())
X = 2.0 #float(input())
arr = dict()

start_time = time.time()
print(f"Простая рекурсия: {P(N, X)}, за {time.time() - start_time} секунд")
start_time = time.time()
print(f"Кэшированная рекурсия: {P_smart(N, X, arr)}, за {time.time() - start_time} секунд")
start_time = time.time()
print(f"Итерационная функция: {P_no_recursia(N, X)}, за {time.time() - start_time} секунд")



