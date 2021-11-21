""" Цикл while похож на оператор if в том смысле, что он выполняет некоторый код, если выполняется некоторое условие.
 Основное отличие состоит в том, что он будет продолжать выполнять тело цикла до тех пор, пока условие имеет значение True.
"""

square = 1

while square <= 10:
    print(square)  # Эта операция выполнится 10 раз
    square += 1  # Эта операция выполнится 10 раз
print("Finished")  # Эта операция выполнится один раз

square = 0
number = 1

# Выведите квадраты чисел от 1 до 9 (1, 4, ... , 81). Используйте числовую переменную в цикле while.

while number <= 9:
    square = number ** 2
    print(square)
    number += 1

# -------------------------------------------------#


""" Бесконечный цикл - это цикл, который никогда не завершается. 
Если условие цикла всегда истинно, такой цикл становится бесконечным. 
Ключевое слово break используется для выхода из текущего цикла. 
"""

count = 0
while True:  # это условие всегда истинно
    print(count)
    count += 1
    if count >= 5:
        break  # выйти из цикла, если count >= 5

# Выйдите из вечного цикла, правильно использовав break

zoo = ["lion", 'tiger', 'elephant']
while True:  # это условие всегда истинно
    animal = zoo.pop()  # извлечь элемент с конца списка
    if animal == 'elephant':
        break
    print(animal)

# выйдите из цикла, когда текущее животное - это 'elephant'


# -----------------------------------------------#


""" 
Ключевое слово continue используется для пропуска остальной части кода внутри текущего выполняемого цикла и возврата к оператору for или while. 
"""

for i in range(5):
    if i == 3:
        continue  # пропустить остаток кода внутри цикла для заданного значения i
    print(i)

# Выведите только нечетные числа 1, 3, 5, 7, 9.

for x in range(10):
    if x % 2 == 0:  # Проверьте х на четность
        continue  # пропустить print(x)
    print(x)