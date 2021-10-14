def fib(n):
    if n in (0,1):
        return 1
    else:
        return fib(n-1) + fib(n - 2)


file_input = open('fib.in', 'r')
file_output = open('fib.out', 'w')

N = int(file_input.readline())
file_output.write(str(fib(N)))

file_input.close()
file_output.close()