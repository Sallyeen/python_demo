# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program: 9 Then, the output should be: 11106

# ---------------mine第一次，未理解题意，不对-------------
# n = input("Please input an integer: ")
# def floor_sum(n):
#     return 

# 最笨的方法
# n = int(input("Please input an integer: "))
# a = n * 1000 + n * 100 + n * 10 + n * 1 + n * 100 + n * 10 + n * 1 + n * 10 + n * 1 + n
# print(a)

# 第二笨
# n = int(input("Please input an integer: "))
# a = n * 1000 + n * 100 * 2 + n * 10 * 3 + n * 4 
# print(a)

a = input()
total = int(a) + int(2*a) + int(3*a) + int(4*a)  # N*a=Na, for example  a="23", 2*a="2323",3*a="232323"
print(total)