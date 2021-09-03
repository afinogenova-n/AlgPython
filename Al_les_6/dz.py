# Определить является ли год, который ввел пользователь, високосным или не високосным.

# Года являюся високосными, если они делятся на 4.
# Исключение составляют года, делящиеся на 100. Они относятся к високосным только при условии что делятся на 400.


from memory_profiler import profile
import sys


@profile
def fun_year(year):
    if year % 4 != 0:
        print(f'{year} не является високосным')
    elif year % 100 == 0:
        if year % 400 == 0:
            print(f'{year} является високосным')
        else:
            print(f'{year} не является високосным')
    else:
        print(f'{year} является високосным')

year = 1985
fun_year(year)

print(f'sys.getsizeof = {sys.getsizeof(fun_year(year))}')

# 1985 не является високосным
# Filename: C:\Users\Настасья\Desktop\PycharmProjects\AlgPython\Al_les_6\dz.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     12     18.1 MiB     18.1 MiB           1   @profile
#     13                                         def fun_year(year):
#     14     18.1 MiB      0.0 MiB           1       if year % 4 != 0:
#     15     18.1 MiB      0.0 MiB           1           print(f'{year} не является високосным')
#     16                                             elif year % 100 == 0:
#     17                                                 if year % 400 == 0:
#     18                                                     print(f'{year} является високосным')
#     19                                                 else:
#     20                                                     print(f'{year} не является високосным')
#     21                                             else:
#     22                                                 print(f'{year} является високосным')
#
#
# sys.getsizeof = 16
