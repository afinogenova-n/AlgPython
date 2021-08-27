'''
Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
Результаты анализа сохранить в виде комментариев в файле с кодом.
'''

import cProfile

def natur_num_1(n):
    a = [0] * n                  # создание массива с n количеством элементов
    for i in range(n):            # заполнение массива ...
        a[i] = i                   # значениями от 0 до n-1

    # вторым элементом является единица, которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0

    m = 2                       # замена на 0 начинается с 3-го элемента (первые два уже нули)
    while m < n:                # перебор всех элементов до заданного числа
        if a[m] != 0:           # если он не равен нулю, то
            j = m * 2           # увеличить в два раза (текущий элемент простое число)
            while j < n:
                a[j] = 0        # заменить на 0
                j = j + m       # перейти в позицию на m больше
        m += 1

    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
    return b


def natur_num_2(n):
    b = []
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            b.append(i)
    return b

def main(n):
    a = natur_num_1(n)
    b = natur_num_2(n)


n = int(input('Введите число, до которого будем искать простые числа: '))

cProfile.run('main(n)')

# Введите число, до которого будем искать простые числа: 876
#          306 function calls in 0.008 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.008    0.008 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 les_04_dz_02.py:11(natur_num_1)
#         1    0.006    0.006    0.006    0.006 les_04_dz_02.py:36(natur_num_2)
#         1    0.000    0.000    0.008    0.008 les_04_dz_02.py:46(main)
#         1    0.000    0.000    0.008    0.008 {built-in method builtins.exec}
#       300    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Введите число, до которого будем искать простые числа: 8760
#          2190 function calls in 0.593 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.593    0.593 <string>:1(<module>)
#         1    0.007    0.007    0.007    0.007 les_04_dz_02.py:11(natur_num_1)
#         1    0.585    0.585    0.585    0.585 les_04_dz_02.py:36(natur_num_2)
#         1    0.000    0.000    0.593    0.593 les_04_dz_02.py:46(main)
#         1    0.000    0.000    0.593    0.593 {built-in method builtins.exec}
#      2184    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

'''
natur_num_1:  линейная сложность
876 элементов за 0,001
8760 элементов за 0,007
natur_num_2:  квадратичная сложность
876 элементов за 0,006
8760 элементов за 0,585
'''