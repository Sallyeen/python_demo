# By using list comprehension, please write a program to print the list after removing the 
# 0th,4th,5th numbers in [12,24,35,70,88,120,155].

lst = [12,24,35,70,88,120,155]
lst.remove(lst[0])
lst.remove(lst[5])
lst.remove(lst[4])
print(lst)