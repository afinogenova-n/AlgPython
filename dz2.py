# По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b,
# проходящей через эти точки


import sys
from memory_profiler import profile

@profile
def fun(x1, x2, y1, y2):
    k=(y1-y2)/(x1-x2)
    b=y1-k*x1
    return f'Уравнение прямой, проходящей через эти две точки: y = {k:.2f}x + {b:.2f}'

y1=3
y2=4
x1=2
x2=6

fun(x1, x2, y1, y2)

print(f'sys.getsizeof(fun(x1, x2, y1, y2) = {sys.getsizeof(fun(x1, x2, y1, y2))}')

k=(y1-y2)/(x1-x2)
b=y1-k*x1
print(f'Уравнение прямой, проходящей через эти две точки: y = {k:.2f}x + {b:.2f}')

print(f'sys.getsizeof(k) = {sys.getsizeof(k)}')
print(f'sys.getsizeof(b) = {sys.getsizeof(b)}')


# C:\Users\Настасья\Desktop\PycharmProjects\AlgPython\venv\Scripts\python.exe C:/Users/Настасья/Desktop/PycharmProjects/AlgPython/dz2.py
# Filename: C:\Users\Настасья\Desktop\PycharmProjects\AlgPython\dz2.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#      4     18.1 MiB     18.1 MiB           1   @profile
#      5                                         def fun(x1, x2, y1, y2):
#      6     18.1 MiB      0.0 MiB           1       k=(y1-y2)/(x1-x2)
#      7     18.1 MiB      0.0 MiB           1       b=y1-k*x1
#      8     18.1 MiB      0.0 MiB           1       return f'Уравнение прямой, проходящей через эти две точки: y = {k:.2f}x + {b:.2f}'
#
#
# sys.getsizeof(fun(x1, x2, y1, y2) = 206
# Уравнение прямой, проходящей через эти две точки: y = 0.25x + 2.50
# sys.getsizeof(k) = 24
# sys.getsizeof(b) = 24

