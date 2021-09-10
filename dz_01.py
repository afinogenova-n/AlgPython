'''
Определение количества различных подстрок с использованием хэш-функции. Пусть дана
строка S длиной N, состоящая только из маленьких латинских букв. Требуется найти
количество различных подстрок в этой строке.
'''


import hashlib
import random
import string

def substr(source_str):

    source_str = str(source_str).lower()

    hash_set = set()

    for i in range(len(source_str)):
        for j in range(len(source_str), i, -1):
            h = hashlib.sha1(source_str[i:j].encode('utf-8')).hexdigest()
            hash_set.add(h)

    return len(hash_set)

def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string

N = int(input('Введите длинну строки: '))

s = generate_random_string(N)
print(s)
print(f'Количество различных подстрок в строке {s}: {substr(s)}')


