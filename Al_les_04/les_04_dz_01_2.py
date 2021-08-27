'''
Проанализировать скорость и сложность одного любого алгоритма, разработанных
в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
'''

# les_02_dz_4
'''
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
'''


import cProfile


# вариант 1

def fun_1(n):
    n = int(n)
    el = 1                          # элементы (начинаются с 1)
    sum_el = 0                      # сумма элементов
    for i in range(n):
        sum_el += el
        el = el / -2
    return f'Сумма элементов {sum_el}'



# вариант 2
def fun_sum_el(n, sum_el=0, el=1):
    n = int(n)
    return f'Сумма эл-в {sum_el}' if (n == 0) else fun_sum_el(n - 1, sum_el=sum_el + el, el=el / -2)


def main(n):
    a = fun_1(n)
    b = fun_sum_el(n, sum_el=0, el=1)

n = int(input('Введите количество элементов: '))

cProfile.run('main(n)')

# Введите количество элементов: 970
#          976 function calls (6 primitive calls) in 0.004 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_04_dz_01_2.py:13(fun_1)
#     971/1    0.004    0.000    0.004    0.004 les_04_dz_01_2.py:25(fun_sum_el)
#         1    0.000    0.000    0.004    0.004 les_04_dz_01_2.py:30(main)
#         1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Введите количество элементов: 500
#          506 function calls (6 primitive calls) in 0.002 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_04_dz_01_2.py:13(fun_1)
#     501/1    0.002    0.000    0.002    0.002 les_04_dz_01_2.py:25(fun_sum_el)
#         1    0.000    0.000    0.002    0.002 les_04_dz_01_2.py:30(main)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# попробовала протестить только fun_1, т.к. fun_sum_el после опред. кол-ва элементов выдает ошибку

# Введите количество элементов: 10000
#          5 function calls in 0.002 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.002    0.002    0.002    0.002 les_04_dz_01_2.py:13(fun_1)
#         1    0.000    0.000    0.002    0.002 les_04_dz_01_2.py:30(main)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Введите количество элементов: 100000
#          5 function calls in 0.015 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.015    0.015 <string>:1(<module>)
#         1    0.015    0.015    0.015    0.015 les_04_dz_01_2.py:13(fun_1)
#         1    0.000    0.000    0.015    0.015 les_04_dz_01_2.py:30(main)
#         1    0.000    0.000    0.015    0.015 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Введите количество элементов: 1000000
#          5 function calls in 0.142 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.142    0.142 <string>:1(<module>)
#         1    0.142    0.142    0.142    0.142 les_04_dz_01_2.py:13(fun_1)
#         1    0.000    0.000    0.142    0.142 les_04_dz_01_2.py:30(main)
#         1    0.000    0.000    0.142    0.142 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

'''
fun_1:   линейная сложность
10000 элементов отрабатывает за 0,002 сек
100000 элементов отрабатывает за 0,015
1000000 элементов отрабатывает за 0,142

fun_sum_el:   наверное, тоже линейная сложность
500 элементов за 0,002
970 элементов за 0,004
дальше выдает ошибку
'''