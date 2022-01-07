# Write a program which can compute the factorial of a given numbers.The results should be printed 
# in a comma-separated sequence on a single line.Suppose the following input is supplied to the program:
#  8 Then, the output should be:40320



# ---------------mine-------------
'''n = int(input("Please input an integer: "))
ans = 1
for i in range(1, n+1):
    ans = ans * i
print(ans)'''

# 别人的  递归调用函数
'''def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x = int(raw_input())
print fact(x)'''

# offical while loop
'''n = int(input("Please input an integer: "))
ans = 1
i = 1
while i <= n:
    ans = ans * i
    i += 1
print(ans)'''

# lambda function
n = int(input())
def shortFact(x): return 1 if x <= 1 else x*shortFact(x-1)
print(shortFact(n))