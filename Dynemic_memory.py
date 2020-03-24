# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# b. написать 3 варианта кода (один у вас уже есть);
# проанализировать 3 варианта и выбрать оптимальный;
# c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# d. написать общий вывод: какой из трёх вариантов лучше и почему.
# Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой переменной, а проявили творчество, фантазию и создали универсальный код для замера памяти.

import sys
# print(sys.version, sys.platform)
# 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] win32

# Задача - посчитать четные и нечетные цифры введенного натурального числа.
# # Например, если введено число 34560, в нем 3 четные цифры
# (4, 6 и 0) и 2 нечетные (3 и 5).


def var1(num):
    c = nc = 0
    sum_size = sys.getsizeof(c) + sys.getsizeof(nc)
    for i in range(len(str(num))):
        num2 = num % 10
        sum_size += sys.getsizeof(num2)
        if num2 % 2 == 0:
            c += 1
            sum_size += sys.getsizeof(c)
        else:
            nc += 1
            sum_size += sys.getsizeof(nc)
        num //= 10
        sum_size += sys.getsizeof(num)
    return sum_size


def var2(num):
    c = 0
    nc = 0
    sum_size = sys.getsizeof(c) + sys.getsizeof(nc)
    for i in str(num):
        if int(i) % 2 == 0:
            c += 1
            sum_size += sys.getsizeof(int(i))
            sum_size += sys.getsizeof(c)
        else:
            nc += 1
            sum_size += sys.getsizeof(nc)
    return sum_size


def var3(num):
    l_chet = [i for i in range(0, 9, 2)]
    sum_size = sys.getsizeof(l_chet)
    l_ne_chet = [i for i in range(1, 10, 2)]
    sum_size += sys.getsizeof(l_ne_chet)
    c = 0
    nc = 0
    sum_size += sys.getsizeof(c)
    sum_size += sys.getsizeof(nc)
    for i in str(num):
        for l in l_chet:
            sum_size += sys.getsizeof(l)
            if int(i) == l:
                sum_size += sys.getsizeof(int(i))
                c += 1
                sum_size += sys.getsizeof(c)
        for l in l_ne_chet:
            if int(i) == l:
                sum_size += sys.getsizeof(int(i))
                nc += 1
                sum_size += sys.getsizeof(nc)
    return sum_size

# a = int(input('Введите число: '))
a = 123145696789764563213216897777323565

print(var1(a), var2(a), var3(a))
# второй вариант занимает меньше памяти. Следует использовать его.

