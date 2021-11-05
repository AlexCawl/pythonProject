# №2
# Сформулируйте алгоритм определения времени года по номеру месяца

month_number = int(input('Введите номер месяца: '))
if month_number in (1, 2, 12):
    print('Зима')
elif month_number in (3, 4, 5):
    print('Весна')
elif month_number in (6, 7, 8):
    print('Лето')
elif month_number in (9, 10, 11):
    print('Осень')
else:
    print('Неверные входные данные')


