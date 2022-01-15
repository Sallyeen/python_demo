# With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make 
# a list whose elements are intersection of the above given lists.

lst1 = [12,24,35,70,88,120,155]
lst2 = [1,3,6,78,35,55]
ans = []
for i in lst1:
    if i in lst2:
        ans.append(i)

print(ans)