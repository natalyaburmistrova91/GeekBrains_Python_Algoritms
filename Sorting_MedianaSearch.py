# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы.
import random


def meridian_finder(array):
    n = 0
    while n <= len(array):
        left = []
        right = []
        middle = []
        meridian = array[n]
        for i in array:
            if i < meridian:
                left.append(i)
            elif i > meridian:
                right.append(i)
            else:
                middle.append(i)
        if len(middle) % 2 == 1 and len(left) == len(right):
            return meridian
        elif len(middle) % 2 == 0 and abs(len(left) - len(right)) == 1:
            return meridian
        else:
            n += 1


array = [random.randint(-100, 100) for i in range(15)]
print(array)
print(sorted(array)) # для проверки
print(meridian_finder(array))


