# Write a method which can calculate square value of number
def cal_square(n):
    return n ** 2

for i in range(5):
    ans = cal_square(i)
    print('The square of {0} is: {1}'.format(i, ans))
