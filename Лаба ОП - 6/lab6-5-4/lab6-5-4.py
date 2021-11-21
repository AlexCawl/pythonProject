from datetime import datetime as dt
import time
import calculated_module

f_input = open('input.txt', 'r')
f_output = open('output.txt', 'w')

start_time = time.time()
current_time = dt.now()

radius = float(f_input.readline())
x, y = list(map(float, f_input.readline().split()))

f_output.write(f'{current_time.day}.{current_time.month}.{current_time.year} {current_time.hour}:{current_time.minute}' + '\n')
f_output.write(f'{calculated_module.points(x, y, radius)}' + '\n')
f_output.write(f'{time.time() - start_time}')

f_input.close()
f_output.close()