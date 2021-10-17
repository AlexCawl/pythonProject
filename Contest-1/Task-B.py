file_input = open('product.in', 'r')
file_output = open('product.out', 'w')

a, b = map(int, file_input.readline().split())
file_output.write(str(a * b))

file_input.close()
file_output.close()