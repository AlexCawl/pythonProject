file_input = open('gcd.in', 'r')
file_output = open('gcd.out', 'w')

a, b = map(int, file_input.readline())
while a != b:
    if a > b:
        a -= b
    else:
        b -= a

file_output.write(str(a))

file_input.close()
file_output.close()