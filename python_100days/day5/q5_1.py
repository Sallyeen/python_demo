# 寻找水仙花数
# ans = []
# for i in range(100,1000):
#     # i_list = str(i).split()
#     a = int(i % 10)
#     b = int((i - a) / 10 % 10)
#     c = int(round((i - b - b * 10) / 100 % 10))
#     print(a, b, c)
#     if a ** 3 + b ** 3 + c ** 3 == i:
#         ans.append(i)
# print(ans)

# for num in range(100, 1000):
#     low = num % 10
#     mid = num // 10 % 10
#     high = num // 100
#     if num == low ** 3 + mid ** 3 + high ** 3:
#         print(num)

for num in range(100, 1000):
    ans = str(num)
    if num == int(ans[0]) ** 3 + int(ans[1]) ** 3 + int(ans[2]) ** 3:
        print(num)

