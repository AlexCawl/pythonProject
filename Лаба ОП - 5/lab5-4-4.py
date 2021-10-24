def ruble_conjugation(n):
    if n % 100 in (11, 12, 13, 14):
        return "РУБЛЕЙ"
    elif n % 10 == 1:
        return "РУБЛЬ"
    elif n % 10 in (2, 3, 4):
        return "РУБЛЯ"
    elif n % 10 in (0, 5, 6, 7, 8, 9):
        return "РУБЛЕЙ"


def kopeck_conjugation(m):
    if m % 100 in (11, 12, 13, 14):
        return "КОПЕЕК"
    elif m % 10 == 1:
        return "КОПЕЙКА"
    elif m % 10 in (2, 3, 4):
        return "КОПЕЙКИ"
    elif m % 10 in (0, 5, 6, 7, 8, 9):
        return "КОПЕЕК"


money_check = int(input())
rubles = money_check // 100
kopecks = money_check % 100
print(rubles, ruble_conjugation(rubles))
print(kopecks, kopeck_conjugation(kopecks))
