#file_input = open('fib.in', 'r')
#file_output = open('fib.out', 'w')

#n = int(file_input.readline().strip())
n = int(input())
fib1, fib2 = 1, 1
for i in range(n):
    fib1, fib2 = fib2, fib1 + fib2
#file_output.write(str(fib1))
print(fib1)
#file_input.close()
#file_output.close()
