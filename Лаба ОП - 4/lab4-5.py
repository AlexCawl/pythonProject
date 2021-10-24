#Напишите программу ("lab4-5.py"), которая считывала бы с клавиатуры данные о пяти призывниках
#(Фамилия, Имя, Отчество, год рождения, заболевание)
# и выводила бы результат в виде таблицы на экран (считывание и сохранение данных должно производится в словарь).

recruit_table = {}
print("Начинаем запись: ")
for i in range(5):
    print("Призывник №", i + 1, sep='')
    surname = input("Фамилия:\t\t")
    name = input("Имя:\t\t\t")
    second_name = input("Отчество:\t\t")
    year = input("Год рождения:\t")
    disease = input("Заболевание:\t")
    recruit_table.update({i+1: ' '.join([surname, name, second_name, year, disease])})

for recruits in recruit_table:
    print(recruits, recruit_table[recruits])


