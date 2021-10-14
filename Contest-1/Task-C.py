file_input = open('apbtest.in', 'r')
file_output = open('apbtest.out', 'w')

summa = int(file_input.readline())

file_output.write(' '.join([str(0), str(summa)]))

file_input.close()
file_output.close()


