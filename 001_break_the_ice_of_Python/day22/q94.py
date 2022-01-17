# Write a program to solve a classic ancient Chinese puzzle: We count 35 heads and 94 legs 
# among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
# 35个头，94只脚，多少只鸡和兔，鸡max35，兔max26

# for i in range(1, 36):
#     for j in range(1, 27):
#         if i + j == 35 and 2 * i + 4 * j == 94:
#             print("共有鸡%d只，兔%d只" % (i, j))


for j in range(1, 27):
    i = 35 - j
    if 2 * i + 4 * j == 94:
        print("共有鸡%d只，兔%d只" % (i, j))




