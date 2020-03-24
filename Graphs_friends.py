# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?

n = int(input('Введите количество встретившихся друзей: '))
friends = []
sum_touch = 0
for i in range(n):
    friends_inner = []
    for l in range(n):
        if i == l:
            friends_inner.append(0)
        else:
            friends_inner.append(1)
    sum_touch += sum(friends_inner)
    friends.append(friends_inner)
print('Полученный граф:')
print(*friends, sep='\n')
print(f'Количество рукопожатий: {sum_touch}')