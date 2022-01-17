# Define a function that can accept two strings as input and print the string with maximum length 
# in console. If two strings have the same length, then the function should print all strings line by line.

# ----------------自写法一--------------
# def long_str(a, b):
#     print(a if len(a) >= len(b) else b)
#     if len(a) == len(b):
#         print(b)

# long_str('Beautiful ', 'Alice')    
# long_str('Beaut', 'Alice')    

func = lambda a,b: print(max((a,b),key=len)) if len(a)!=len(b) else print(a+'\n'+b)