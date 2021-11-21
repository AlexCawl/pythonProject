def is_input_file_here(name, files):
    text_file_counter = 0
    is_input_txt_here = False

    for file_name in files:
        if os.path.isfile(file_name):
            text_file_counter += 1
        if file_name == name:
            is_input_txt_here = True

    return [is_input_txt_here, text_file_counter]


def summa(n):
    res = 0
    for digit in n:
        res += int(digit)
    return str(res)


def multiplication(n):
    res = 1
    for digit in n:
        res *= int(digit)
    return str(res)


import os

file_list = set(os.listdir())
f_output = open('output.txt', 'w')

if is_input_file_here('input.txt', file_list)[0]:
    f_input = open('input.txt', 'r')
    number = f_input.readline()
    if number == '':
        f_output.write("Файл с входными данными не обнаружен")
        f_output.close()
    else:
        if ' ' in number:
            number = number.split()[0]

        f_output.write("Число: " + str(number) + "\n")
        f_output.write("Количество цифр: " + str(len(number)) + "\n")
        f_output.write("Сумма цифр: " + str(summa(number)) + "\n")
        f_output.write("Произведение цифр: " + str(multiplication(number)) + "\n")
        f_input.close()
else:
    f_output.write("Файл с входными данными не обнаружен")
    f_output.close()