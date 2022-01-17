# Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES"
#  or "Yes", otherwise print "No".

# -----------自写法一------------------------
# seq = input("Input")
# ans = 'Yes' if seq == "yes" or seq == "YES" or seq == "Yes" else 'No'
# print(ans)

# 不完全对，思想不错
seq = input("Input").lower()
ans = 'Yes' if seq == "yes" else 'No'
print(ans)