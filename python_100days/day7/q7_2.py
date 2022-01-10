# 设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。

import random

def generate_code(len_code=4):
    res = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
    n = len(res)
    ans = ''
    for _ in range(4):
        rand_n = random.randint(0, n-1)
        ans += res[rand_n]
    return ans

ans = generate_code(4)
inp = input("请输入验证码：")
if inp == ans:
    print("Welcome！")
else:
    print("error")

