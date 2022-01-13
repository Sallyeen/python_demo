# Define a function that can receive two integer numbers in string form and compute their sum 
# and then print it in console.

# --------------自写法一－－－－－－－－－－－－－－
# def sum_str(a,b):
#     a, b = int(a), int(b)
#     print(a+b)

# sum_str('2','3')

# ------------------自写法二--------------------------
sum_str = lambda a, b: int(a) + int(b)
print(sum_str('2','3'))