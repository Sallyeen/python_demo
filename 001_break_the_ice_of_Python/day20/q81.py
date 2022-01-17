# By using list comprehension, please write a program to print the list after removing numbers 
# which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

lst = [12,24,35,70,88,120,155]
ans = filter(lambda i: i % 5 != 0 or i % 7 != 0, lst)
print(list(ans))
