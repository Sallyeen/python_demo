# Please write a binary search function which searches an item in a sorted list. The function 
# should return the index of element to be searched in the list.

lst = [1, 3, 4, 6]
n = len(lst)
left,right = 0, n-1
a = int(input("Input a number:"))
while left < right:
    if lst[(right+left) // 2] < a:
        left = (right+left) // 2 + 1
    else:
        right = (right+left) // 2 - 1
print(lst[left])
