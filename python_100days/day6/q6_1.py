# 实现计算求最大公约数和最小公倍数的函数
import math

def max_(a, b):
    for i in range(int(math.sqrt(max(a,b))), 0, -1):
        if a % i == 0 and b % i == 0:
            return i

def min_(a, b):
    for i in range(max(a,b), a*b+1):
        if i % a == 0 and i % b == 0:
            return i

ans1 = max_(int(input()), int(input()))
print("最大公约数为:", ans1)
ans2 = min_(int(input()), int(input()))
print("最小公倍数为:", ans2)
