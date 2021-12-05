def C(n, m, cache):
    if (n, m) in cache:
        return cache[(n, m)]

    if m == 0 or n == m:
        cache.update({(n, m): 1})
    else:
        cache.update({(n, m): C(n - 1, m, cache) + C(n - 1, m - 1, cache)})
    return cache[(n, m)]


arr = dict()
N, M = list(map(int, input().split()))
print(C(N, M, arr))

