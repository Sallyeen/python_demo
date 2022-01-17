# Write a program which can filter() to make a list whose elements are even number between 
# 1 and 20 (both included).

lst = input("Input a list: ").split()
ans = filter(lambda i: int(i) >= 1 and int(i) <= 20 and int(i) % 2 ==0, lst)
ans = map(lambda i: int(i), ans)
print(list(ans))