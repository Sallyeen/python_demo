# 设计一个函数返回传入的列表中最大和第二大的元素的值

# def max_value(lst):
#     '''
#     返回传入的列表中最大和第二大的元素的值

#     lst:传入的列表
#     ans:最大和第二大的元素的值
#     '''
#     # ans1 = max(lst)
#     # lst.remove(int(ans1))
#     # ans2 = max(lst)
#     lst = sorted(lst)
#     lst = "".join(lst)
#     return lst[-1], lst[-2]

def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0]) # 前两个数按大到小排列
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2

# demo = max_value(input().split())
# print(demo)
