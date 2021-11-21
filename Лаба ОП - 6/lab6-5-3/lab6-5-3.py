def is_input_file_here(name):
    is_input_txt_here = False
    file_list = set(os.listdir())

    for file_name in file_list:
        if file_name == name:
            is_input_txt_here = True
            break

    return is_input_txt_here


def prime(x):
    if x in [0, 1]:
        return False
    if x == 2:
        return True
    for n in range(2, int(x ** 0.5 + 1)):
        if x % n == 0:
            return False
    return True


import os
f_output = open('output.txt', 'w')

if is_input_file_here('input.txt'):
    f_input = open('input.txt', 'r')
    number = int(f_input.readline())

    for i in range(1, number):
        if prime(i):
            f_output.write(str(i) + ' ')
    f_input.close()
else:
    f_output.write('Файл с входными данными не обнаружен')
f_output.close()
