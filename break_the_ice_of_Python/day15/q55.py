# Write a program which accepts a sequence of words separated by whitespace as input to print 
# the words composed of digits only. Example: If the following words is given as input to the program:
# 2 cats and 3 dogs. Then, the output of the program should be: ['2', '3']

# 法一，避开了正则表达式
# seq = input('Input:').split()
# ans = []
# for item in seq:
#     if item.isdigit():
#         ans.append(item)
# print(ans)


import re

seq = input('Input:')
pattern = "\d+"
ans = re.findall(pattern,seq)
print(ans)