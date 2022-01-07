# 寻找输入的反转
n = int(input("输入一个数："))
ans = 0
while True:
    if n == 0:
        break
    ans = n % 10 + 10 * ans
    n  = n // 10
print(ans)

# num = int(input('num = '))
# reversed_num = 0
# while num > 0:
#     reversed_num = reversed_num * 10 + num % 10
#     num //= 10
# print(reversed_num)
