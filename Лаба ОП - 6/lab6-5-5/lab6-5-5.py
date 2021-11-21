def matrix_printing(i, j, matrix):
    for n in range(i):
        for m in range(j):
            f_output.write(f'{matrix[n][m]:07.3f}' + ' ')
        f_output.write('\n')
    f_output.write('\n')


def matrix_chaotic(matrix_old):
    for k in range(len(matrix_old)):
        current_lay = matrix_old[k]
        local_max = max(current_lay)
        for t in range(len(current_lay)):
            current_lay[t] = float(current_lay[t]) / float(local_max)


import numpy

f_input = open('input.txt', 'r')
f_output = open('output.txt', 'w')
N, M = list(map(int, f_input.readline().split()))

matrix_A = [[numpy.random.randint(1, 100) for m in range(M)] for n in range(N)]
matrix_printing(N, M, matrix_A)

matrix_A_new = []
matrix_chaotic(matrix_A)
matrix_printing(N, M, matrix_A)

K = numpy.random.randint(5, 15)
matrix_B = [[numpy.random.randint(1, 100) for k in range(K)] for m in range(M)]
matrix_printing(M, K, matrix_B)

matrix_C = numpy.dot(matrix_A, matrix_B)
matrix_printing(N, K, matrix_C)

