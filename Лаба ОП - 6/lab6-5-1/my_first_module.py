def PrintRectangle(a, b, file):
    f_output = open(file, 'w')

    top = '* ' * a
    bottom = '* ' + '  ' * (a - 2) + '* '

    f_output.write(top + '\n')
    if b > 1:
        for i in range(b - 2):
            f_output.write(bottom + '\n')
        f_output.write(top + '\n')

    f_output.close()


def PrintSquare(a, file):
    f_output = open(file, 'w')

    top = '* ' * a
    bottom = '* ' + '  ' * (a - 2) + '* '
    f_output.write(top + '\n')
    if a > 1:
        for i in range(a - 2):
            f_output.write(bottom + '\n')
        f_output.write(top + '\n')

    f_output.close()