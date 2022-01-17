# By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 
# 4th,6th numbers in [12,24,35,70,88,120,155].

lst = [12,24,35,70,88,120,155]
ans = []
for i in range(len(lst)):
    if i % 2 != 0:
        ans.append(lst[i])
print(ans)