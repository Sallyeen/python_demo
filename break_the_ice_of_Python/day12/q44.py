# Write a program which can map() to make a list whose elements are square of numbers 
# between 1 and 20 (both included).

ans = map(lambda i: i ** 2, range(1, 21))
print(list(ans))