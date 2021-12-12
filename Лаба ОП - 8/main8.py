import sorts
import time
import random


N = int(input())
sequence = [random.randint(1, N) for i in range(N)]
sequence_sorted = sorted(sequence)
sequence_reversed = sorted(sequence, reverse=True)

file_output = open('output.txt', 'w')
file_output.write(f"количество элементов: {N}\n")
file_output.write(f"случайная последовательность, сгенерированная программно: {sequence}\n\n")

# пузырьковая сортировка
time_1_1 = time.time()
method_1_1 = sorts.bubble_sort(sequence)
time_1_1 = time.time() - time_1_1

time_1_2 = time.time()
method_1_2 = sorts.bubble_sort(sequence_sorted)
time_1_2 = time.time() - time_1_2

time_1_3 = time.time()
method_1_3 = sorts.bubble_sort(sequence_reversed)
time_1_3 = time.time() - time_1_3
file_output.write(f"{'Пузырьковая сортировка:':23} отсортированная - {time_1_2:10.7f}, случайная - {time_1_1:10.7f}, "
                  f"отсортированная в обратном порядке - {time_1_3:10.7f}\n")

# сортировка слиянием
time_2_1 = time.time()
method_2_1 = sorts.merge_sort(sequence)
time_2_1 = time.time() - time_2_1

time_2_2 = time.time()
method_2_2 = sorts.merge_sort(sequence_sorted)
time_2_2 = time.time() - time_2_2

time_2_3 = time.time()
method_2_3 = sorts.merge_sort(sequence_reversed)
time_2_3 = time.time() - time_2_3
file_output.write(f"{'Сортировка слиянием:':23} отсортированная - {time_2_2:10.7f}, случайная - {time_2_1:10.7f}, "
                  f"отсортированная в обратном порядке - {time_2_3:10.7f}\n")

# быстрая сортировка
time_3_1 = time.time()
sorts.quick_sort(sequence.copy(), 0, len(sequence)-1)
time_3_1 = time.time() - time_3_1

time_3_2 = time.time()
method_3_2 = sorts.quick_sort(sequence_sorted.copy(), 0, len(sequence_sorted)-1)
time_3_2 = time.time() - time_3_2

time_3_3 = time.time()
method_3_3 = sorts.quick_sort(sequence_reversed.copy(), 0, len(sequence_reversed)-1)
time_3_3 = time.time() - time_3_3
file_output.write(f"{'Быстрая сортировка:':23} отсортированная - {time_3_2:10.7f}, случайная - {time_3_1:10.7f}, "
                  f"отсортированная в обратном порядке - {time_3_3:10.7f}\n")

# встроенная сортировка
time_4_1 = time.time()
sequence.copy().sort()
time_4_1 = time.time() - time_4_1

time_4_2 = time.time()
sequence_sorted.copy().sort()
time_4_2 = time.time() - time_4_2

time_4_3 = time.time()
sequence_reversed.copy().sort()
time_4_3 = time.time() - time_4_3
file_output.write(f"{'Встроенная сортировка:':23} отсортированная - {time_4_2:10.7f}, случайная - {time_4_1:10.7f}, "
                  f"отсортированная в обратном порядке - {time_4_3:10.7f}\n")

file_output.close()
