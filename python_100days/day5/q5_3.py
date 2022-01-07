# 公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
import time

# 1.006879
# start = time.clock()
# for k in range(300):
#     if k % 3 != 0:
#         continue
#     for j in range(300):
#         for i in range(300): 
#             if i + j + k == 100 and 5 * i + 3 * j + k / 3 == 100: 
#                 print("公鸡%d只， 母鸡%d只， 小鸡%d只" % (i, j, k))
# end = time.clock()
# print("The whole time is: ", %.2f % end-start)

# 0.000225
# start = time.clock()
# for x in range(0, 20):
#     for y in range(0, 33):
#         z = 100 - x - y
#         if 5 * x + 3 * y + z / 3 == 100:
#             print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))
# end = time.clock()
# print("The whole time is: ", end-start)

# 0.000195
start = time.clock()
for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if z % 3 != 0:
            continue
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))
end = time.clock()
print("The whole time is: ", end-start)