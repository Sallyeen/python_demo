# By using list comprehension, please write a program to print the list after removing the 2nd 
# - 4th numbers in [12,24,35,70,88,120,155].

lst = [12,24,35,70,88,120,155]
lst.remove(lst[2])
lst.remove(lst[3])
lst.remove(lst[4])
print(lst)