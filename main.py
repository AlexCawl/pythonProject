N = int(input().strip())
importance = list(map(int, input().strip().split()))
importance.sort()
counter_current, counter_max = 1, 0

i = 1
while i < len(importance):
    if importance[i - 1] > importance[i] / 2:
        counter_current += 1
    else:
        counter_max = max(counter_current, counter_max)
        counter_current = 1

    counter_max = max(counter_current, counter_max)
    i += 1
counter_max = max(counter_current, counter_max)
print(counter_max)
#1
#24