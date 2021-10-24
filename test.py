import random

def Denis(a):
    for i in range(0, len(a)):
        a1 = a.copy()
        c = i + 1
        if i == 0:
            while (len(a1) != 1) and (a1[i] > a1[i + 1]):
                a1[i] += 1
                a1.pop(i + 1)

            if len(a1) == 1:
                return c

        if i == len(a) - 1:
            while (len(a1) != 1) and (a1[i] > a1[i - 1]):
                a1[i] += 1
                a1.pop(i - 1)
                i = i - 1

            if len(a1) == 1:
                return c

        if i != 0 and i != len(a) - 1:
            while (len(a1) != 1) and (a1[i] > a1[i - 1] or a1[i] > a1[i + 1]) and len(a1) != 0:
                if a1.index(a1[i]) == 0 and a1[i - 1] < a1[i] <= a1[i + 1]:
                    a1 = []
                    break
                if i == len(a1) - 1:
                    pass
                else:
                    if a1[i] > a1[i + 1]:
                        a1[i] += 1
                        a1.pop(i + 1)

                if a1.index(a1[i]) == 0:
                    pass
                else:
                    if a1[i] > a1[i - 1]:
                        a1[i] += 1
                        a1.pop(i - 1)
                        i = i - 1

            if len(a1) == 1:
                return c

        # print(i)
        if i == len(a) - 1 and len(a1) != 1:
            a.append(0)

    if a[-1] == 0:
        return -1


def analysis(aquarium):
    # 1) все элементы равны => выводим -1
    if min(aquarium) == max(aquarium):
        return -2  # вывод
    else:
        # 2) есть только один максимальный элемент
        counter_max = 0
        max_piranha = max(aquarium)
        for piranha in aquarium:
            if piranha == max_piranha:
                counter_max += 1
            if counter_max > 1:
                break

        if counter_max == 1:
            return aquarium.index(max_piranha)
        else:
            # 3) несколько максимумов
            # ищем первый подходящий слева-направо
            for i in range(len(aquarium) - 1):
                if aquarium[i] == max_piranha and aquarium[i] > aquarium[i + 1]:
                    return i
            # ищем первый подходящий справа-налево
            for j in range(len(aquarium) - 1, 0, -1):
                if aquarium[j] == max_piranha and aquarium[j - 1] < aquarium[j]:
                    return j


counter = random.randint(1, 2000)
for k in range(counter):
    counter_2 = random.randint(2, 10)
    aquarium = []
    for m in range(counter_2):
        aquarium.append(random.randint(1, 100))
    print()
    print(aquarium)
    print(k, [analysis(aquarium) + 1, Denis(aquarium)], counter_2, aquarium)

