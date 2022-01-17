# Please write a program which prints all permutations of [1,2,3]

import itertools
lst = [1,2,3]
lst = itertools.permutations(lst)
print(list(lst))