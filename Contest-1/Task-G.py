file_input = open('numbers.in', 'r')
file_output = open('numbers.out', 'w')

a, b = list(map(int, file_input.readline().split()))
x, y = 0, 0
for i in range(a):
    if (1 - b * i) % a == 0:
        y = i
        x = (1 - b * i) // a
        break

file_output.write(str(x) + ' ' + str(y))
file_input.close()
file_output.close()