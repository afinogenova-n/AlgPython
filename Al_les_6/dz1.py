'''
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843.
'''

import sys
from memory_profiler import profile

# 1 вариант
@profile
def new_num_1(num):
    num = str(num)
    new_num = num[::-1]
    return new_num


# 2 вариант
@profile
def new_num_2(num):
    num = int(num)
    new_num = 0
    while num > 0:
        new_num = new_num * 10 + num % 10
        num = num // 10
    return new_num

# 3 вариант
@profile
def number_reversal(num, new_num=0):
    num = int(num)
    return new_num if (num == 0) else number_reversal(num // 10, new_num * 10 + num % 10)

num = 564764

new_num_1(num)

# C:\Users\Настасья\Desktop\PycharmProjects\AlgPython\venv\Scripts\python.exe C:/Users/Настасья/Desktop/PycharmProjects/AlgPython/Al_les_6/dz1.py
# Filename: C:\Users\Настасья\Desktop\PycharmProjects\AlgPython\Al_les_6\dz1.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#      9     18.0 MiB     18.0 MiB           1   @profile
#     10                                         def new_num_1(num):
#     11     18.0 MiB      0.0 MiB           1       num = str(num)
#     12     18.0 MiB      0.0 MiB           1       new_num = num[::-1]
#     13     18.0 MiB      0.0 MiB           1       return new_num


new_num_2(num)

# Filename: C:\Users\Настасья\Desktop\PycharmProjects\AlgPython\Al_les_6\dz1.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     18     18.1 MiB     18.1 MiB           1   @profile
#     19                                         def new_num_2(num):
#     20     18.1 MiB      0.0 MiB           1       num = int(num)
#     21     18.1 MiB      0.0 MiB           1       new_num = 0
#     22     18.1 MiB      0.0 MiB           7       while num > 0:
#     23     18.1 MiB      0.0 MiB           6           new_num = new_num * 10 + num % 10
#     24     18.1 MiB      0.0 MiB           6           num = num // 10
#     25     18.1 MiB      0.0 MiB           1       return new_num

number_reversal(num, new_num=0)

# Filename: C:\Users\Настасья\Desktop\PycharmProjects\AlgPython\Al_les_6\dz1.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     28     18.1 MiB     18.1 MiB           1   @profile
#     29                                         def number_reversal(num, new_num=0):
#     30     18.1 MiB      0.0 MiB           1       num = int(num)
#     31     18.1 MiB      0.0 MiB           1       return new_num if (num == 0) else number_reversal(num // 10, new_num * 10 + num % 10)