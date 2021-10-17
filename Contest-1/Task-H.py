file_input = open('symposium.in', 'r')
file_output = open('symposium.out', 'w')

text = file_input.readlines()
N = int(text[0].strip())
importance = list(map(int, text[1].strip().split()))
importance.sort()
counter_current, counter_max = 1, 0

i = 1
while i < len(importance):
    if importance[i - 1] > importance[i] / 2:
        counter_current += 1
    else:
        counter_max = max(counter_current, counter_max)
        counter_current = 1

    counter_max = max(counter_current, counter_max)
    i += 1
counter_max = max(counter_current, counter_max)

file_output.write(str(counter_max))

file_input.close()
file_output.close()
