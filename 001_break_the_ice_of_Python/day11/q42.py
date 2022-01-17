# Write a program which can map() and filter() to make a list whose elements are square of
#  even number in [1,2,3,4,5,6,7,8,9,10].

lst = [1,2,3,4,5,6,7,8,9,10]
# even_num = filter(lambda i: i % 2 == 0, lst)
# ans = map(lambda i:i ** 2, even_num)
ans = map(lambda i:i ** 2, filter(lambda i: i % 2 == 0, lst))
print(list(ans))