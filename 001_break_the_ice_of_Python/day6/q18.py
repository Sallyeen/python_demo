# A website requires the users to input username and password to register. Write a program to check 
# the validity of password input by users. Following are the criteria for checking the password: 
# At least 1 letter between [a-z] At least 1 number between [0-9] At least 1 letter between [A-Z]
# At least 1 character from [$#@] Minimum length of transaction password: 6 
# Maximum length of transaction password: 12 Your program should accept a sequence of comma 
# separated passwords and will check them according to the above criteria. Passwords that match 
# the criteria are to be printed, each separated by a comma. Example If the following passwords 
# are given as input to the program: ABd1234@1,aF1#,2w3E*,2We3345 Then, the output of the program 
# should be: ABd1234@1

# 只能保证输入序列的每一个元素合法，并不能保证完全
# seq = input("Please input a sequence of passwords:").split(",")
# ans = []
# for i in seq:
#     n = len(i)
#     if n < 6 or n > 12:
#         continue
#     for j in range(n):
#         if i[j] in 'qwertyuiopasdfghjklzxcvbnm' or i[j] in 'QWERTYUIOPASDFGHJKLZXCVBNM' or \
#          i[j] in '1234567890' or i[j] in '$#@':
#             ans.append(i)
#             break

# print(",".join(ans))

import re
value = []
items = [x for x in raw_input().split(',')]
for p in items:
    if len(p) < 6 or len(p) > 12:
        continue
    else:
        pass
    if not re.search("[a-z]",p): # 返回第一个成功的匹配，可以不从第一项开始比较
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif re.search("\s",p):
        continue
    else:
        pass
    value.append(p)
print(",".join(value))
