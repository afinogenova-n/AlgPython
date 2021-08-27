'''
Проанализировать скорость и сложность одного любого алгоритма, разработанных
в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
'''

# les_02_dz_3
'''
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843.
'''

import cProfile



# 1 вариант

def new_num_1(num):
    num = str(num)
    new_num = num[::-1]
    return new_num


# 2 вариант

def new_num_2(num):
    num = int(num)
    new_num = 0
    while num > 0:
        new_num = new_num * 10 + num % 10
        num = num // 10
    return new_num


# 3 вариант

def number_reversal(num, new_num=0):
    num = int(num)
    return new_num if (num == 0) else number_reversal(num // 10, new_num * 10 + num % 10)


def main(num):
    a = new_num_1(num)
    b = new_num_2(num)
    c = number_reversal(num, new_num=0)

num = input('Введите число: ')

cProfile.run('main(num)')


# тут оценить сложность и время практически не возможно, чтобы получить 0,002 сек. у одной ф-ции
# пришлось ввести число с 491 символом, другие две ф-ции так и не шевельнулись
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_04_dz_01.py:19(new_num_1)
#         1    0.000    0.000    0.000    0.000 les_04_dz_01.py:27(new_num_2)
#     492/1    0.002    0.000    0.002    0.002 les_04_dz_01.py:38(number_reversal)
#         1    0.000    0.000    0.003    0.003 les_04_dz_01.py:43(main)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}





