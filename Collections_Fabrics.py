# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.


from collections import defaultdict


number_of_factories = int(input('Введите количество предприятий, участвующих в расчете: '))
list_of_factories = []
list_of_below = []
list_of_above = []
for i in range(number_of_factories):
    name = input('Введите название предприятия: ')
    profit = int(input('Введите прибыль за 4 квартала: '))
    list_of_factories.append((name, profit))
profit = defaultdict(list)
for n, p in list_of_factories:
    profit['profit'].append(p)
aver = sum(profit.get('profit'))/len(profit.get('profit'))
for n, p in list_of_factories:
    if p >= aver:
        list_of_above.append(n)
    else:
        list_of_below.append(n)

print(f'Среднее значение = {aver:.2f}')
print('Предприятия у которых прибыль выше среднего: ')
for i in list_of_above:
    print(f'{i}')
print('Предприятия у которых прибыль ниже среднего: ')
for i in list_of_below:
    print(f'{i}')
