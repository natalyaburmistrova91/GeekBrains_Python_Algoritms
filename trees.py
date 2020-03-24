import binarytree

# # class MyNode:
# #
# #     def __init__(self, data, left=None, right=None):
# #         self.data = data
# #         self.left = left
# #         self.right = right
# #
#
# a = binarytree.tree(height=4, is_perfect=False)
# print(a)
#
# b = binarytree.bst(height=3, is_perfect=True)
# print(b)
#
# c = binarytree.Node(7)
# c.left = binarytree.Node(3)
# c.right = binarytree.Node(11)
# c.left.left = binarytree.Node(1)
# c.left.right = binarytree.Node(5)
# c.right.left = binarytree.Node(9)
# c.right.right = binarytree.Node(13)
#
# print(c)

d = binarytree.build([7, 3, 11, 1, 5, 9, 3])

print(d)

# поиск значения в бинарном дереве
#
# def search(bin_search_tree, number, path=''):
#     if bin_search_tree.value == number:
#         return f'Число {number} обнаружено по следующему пути: \n Корень {path}'
#     if number < bin_search_tree.value and bin_search_tree.left != None:
#         return search(bin_search_tree.left, number, path=f'{path}\nШаг влево')
#     if number > bin_search_tree.value and bin_search_tree.right != None:
#         return search(bin_search_tree.right, number, path=f'{path}\nШаг вправо')
#
#     return f'Число {number} отсутствует в дереве'
#
#
# bt = binarytree.bst(height=5, is_perfect=False)
# print(bt)
# num = int(input('Введите число для поиска: '))
# print(search(bt, num))