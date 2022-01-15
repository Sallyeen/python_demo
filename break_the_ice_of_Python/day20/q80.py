# Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].

# lst = [5,6,77,45,22,12,24]
# for i in lst:
#     if i % 2 == 0:
#         lst.remove(i )
# print(lst)

li = [5,6,77,45,22,12,24]
lst = list(filter(lambda n:n%2!=0,li))
print(lst)