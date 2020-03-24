# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления, задача решается в несколько строк.
# Для прокачки алгоритмического мышления такой вариант не подходит. Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.
# Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.
from collections import ChainMap

DICT_OF_SYSTEM_10 = {
}

DICT_OF_SYSTEM_16 = {
}

def from_10_to_16(list):
    res = 0
    for i in range(len(list)):
        res += dict_of_current.get(list[(len(list) - 1 - i)]) * (16 ** i)
    return res


def from_16_to_10(num):
    list_of_16 = []
    list_of_16_fin = []
    res = ''
    while num >= 15:
        list_of_16.append(num - (num // 16) * 16)
        num //= 16
        if num <= 15:
            list_of_16.append(num)
    for i in reversed(list_of_16):
        list_of_16_fin.append(dict_of_current.get(i))
    for i in list_of_16_fin:
        res += f'{i}'
    return res


def dict_filler():
    for i in range(10):
        DICT_OF_SYSTEM_10[str(i)] = i
        DICT_OF_SYSTEM_10[i] = str(i)
    for l in range(10, 16):
        DICT_OF_SYSTEM_16[chr(l + 55)] = l
        DICT_OF_SYSTEM_16[l] = chr(l + 55)

dict_filler()
dict_of_current = ChainMap(DICT_OF_SYSTEM_10, DICT_OF_SYSTEM_16)

first_number = input('Введите первое число: ')
second_number = input('Введите второе число: ')

first_10 = from_10_to_16(first_number)
second_10 = from_10_to_16(second_number)

sum_10 = first_10 + second_10
pro_10 = first_10 * second_10

sum_16 = from_16_to_10(sum_10)
pro_16 = from_16_to_10(pro_10)

print(sum_16, pro_16)







