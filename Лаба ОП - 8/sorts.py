def merge_sort(arr):
    if len(arr) == 0 or len(arr) == 1:  # бежим пока не будет пустой/единичный массив, который УЖЕ отсортирован
        return arr

    left_part, right_part = merge_sort(arr[:len(arr) // 2]), merge_sort(arr[len(arr) // 2:])
    # получаем отсортированные массивы с предыдущих итераций
    res = []
    while len(left_part) > 0 and len(right_part) > 0:  # собираем массив обратно
        if left_part[0] < right_part[0]:
            res.append(left_part[0])
            left_part.pop(0)
        else:
            res.append(right_part[0])
            right_part.pop(0)
    if len(left_part) > 0:  # собираем остатки с левой (если они есть)
        res.extend(left_part)
    if len(right_part) > 0:  # собираем остатки с правой (если они есть)
        res.extend(right_part)
    return res


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr


def quick_sort(nums, l, r):
    if l >= r:
        return

    i, j = l, r
    bar = nums[i + (j - i) // 2]

    while i <= j:
        while nums[i] < bar:
            i += 1
        while nums[j] > bar:
            j -= 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1
    quick_sort(nums, l, j)
    quick_sort(nums, i, r)
