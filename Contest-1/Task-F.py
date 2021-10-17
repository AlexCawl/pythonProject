file_input = open('skateboard.in', 'r')
file_output = open('skateboard.out', 'w')

text = file_input.readlines()
N = int(text[0].strip())
road = list(map(int, text[1].strip().split()))
counter_zelenka = 0
for i in range(1, len(road)-1):
    if road[i-1] < road[i] > road[i + 1]:
        counter_zelenka += 1

file_output.write(str(counter_zelenka))

file_input.close()
file_output.close()
