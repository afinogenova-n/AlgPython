'''
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и
отсортированный массивы.
'''

from random import randint


list_1 = []
for i in range(10):
    list_1.append(randint(0, 50))
print(f'Исходный список:\n {list_1}')


def merge_sort(obj):
    if len(obj) <= 1:
        return obj
    else:
        left_list = merge_sort(obj[:len(obj) // 2])
        right_list = merge_sort(obj[len(obj) // 2:])
        return merge(left_list, right_list)


def merge(left_list, right_list):
    sorted_list = []
    left_list_index, right_list_index = 0, 0

    for i in range(len(left_list) + len(right_list)):
        if left_list_index < len(left_list) and right_list_index < len(right_list):
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        elif left_list_index == len(left_list):
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1

        elif right_list_index == len(right_list):
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


print(f'Отсортированный список:\n {merge_sort(list_1)}')