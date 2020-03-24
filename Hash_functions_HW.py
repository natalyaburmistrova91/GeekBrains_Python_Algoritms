# 1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача считается не решённой.
import hashlib


def num_subs(s: str) -> int:
    assert len(s) > 0, 'Строка не может быть пустой'
    hfull = hashlib.sha1(s.encode('utf-8')).hexdigest()
    hempty = hashlib.sha1(''.encode('utf-8')).hexdigest()
    amount_sub = 0

    for i in range(len(s) + 1):
        for l in range(len(s) + 1):
            hsub = hashlib.sha1(s[i:l].encode('utf-8')).hexdigest()
            if hsub != hfull and hsub != hempty:
                amount_sub += 1
    return amount_sub


s = input('Введите строку: ')
print(num_subs(s))
