# The Fibonacci Sequence is computed based on the following formula: f(n)=0 if n=0 f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1 Please write a program to compute the value of f(n) with a given n input
#  by console. Example: If the following n is given as input to the program: 7
# Then, the output of the program should be: 0,1,1,2,3,5,8,13

# def f(n):
#     if n < 2:
#         return n
#     else:
#         return f(n-1) + f(n-2)
# n = int(input("Input a integer: "))
# ans = map(lambda i: str(f(i)), range(0, n+1))
# print(",".join(list(ans)))


f = lambda i: f(i-1) + f(i-2) if i > 1 else i
n = int(input("Input a integer: "))
ans = map(lambda i: str(f(i)), range(0, n+1))
print(",".join(list(ans)))