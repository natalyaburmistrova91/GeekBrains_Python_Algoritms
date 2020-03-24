# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.
# Пример работы программ:
# >>> sieve(2)
# 3
# >>> prime(4)
# 7
# >>> sieve(5)
# 11
# >>> prime(1)
# 2
# Примечание по профилированию кода: для получения достоверных результатов при замере времени необходимо исключить/заменить функции print() и input() в анализируемом коде.
# С ними вы будете замерять время вывода данных в терминал и время, потраченное пользователем, на ввод данных, а не быстродействие самого алгоритма.
import timeit
import cProfile


def resheto(num):
    sieve = [i for i in range(num)]
    sieve[1] = 0
    for i in range(2, num):
        if sieve[i] != 0:
            j = i * 2
            while j < num:
                sieve[j] = 0
                j += i
    return [i for i in sieve if i != 0]


def check_simple_resheto(num):
    k = 2
    a = []
    while len(a) < n:
        a = resheto(k)
        k += 1
    return a


def check_simple(num):
    simple_list = []
    k = 2
    while len(simple_list) < num:
        num_del = 0
        for i in range(1, k + 1):
            if k % i == 0:
                num_del += 1
        if num_del == 2:
            simple_list.append(k)
        k += 1
    return simple_list


n = int(input('Какое по счету простое число вы хотите получить: '))
print(check_simple_resheto(n)[n - 1])
print(check_simple(n)[n - 1])


cProfile.run('check_simple_resheto(n)')
cProfile.run('check_simple(n)')
print(timeit.timeit('check_simple_resheto(15)', setup="from __main__ import check_simple_resheto", number=10000))
# для 100 = 0.04047920000000005
# для 10000 = 4.078847100000001
print(timeit.timeit('check_simple(15)', setup="from __main__ import check_simple", number=10000))
# для 100 = 0.012267500000000098
# для 10000 = 1.0401378999999995

# второй способ оказался быстрее из-за отсутствия постоянного составление нового списка при K += 1
