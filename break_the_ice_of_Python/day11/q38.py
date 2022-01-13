# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in 
# one line and the last half values in one line.

lst = (1,2,3,4,5,6,7,8,9,10)
n = int(len(lst)/2)
print(lst[:n],'\n',lst[n:])