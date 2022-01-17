# Given a number N.Find Sum of 1 to N Using Recursion Input 5 Output 15


def num_add(n):
    if n == 0:
        return 0
    return n + num_add(n-1)
n = int(input("Input a number: "))
ans = num_add(n)
print(ans)