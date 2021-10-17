file_input = open('apbtest.in', 'r')
file_output = open('apbtest.out', 'w')

summa = int(file_input.readline())
if summa % 2 == 0:
    a = b = summa // 2
else:
    a = int(summa/2 + 0.5)
    b = int(summa/2 - 0.5)

file_output.write(str(a) + ' ' + str(b))

file_input.close()
file_output.close()


