# Write a program to generate and print another tuple whose values are even numbers 
# in the given tuple (1,2,3,4,5,6,7,8,9,10).

lst = (1,2,3,4,5,6,7,8,9,10)
lst1 = tuple(i for i in lst if i % 2 == 0)
print(lst1)