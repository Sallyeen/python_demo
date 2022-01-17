# Write a program that calculates and prints the value according to the given formula: Q = 
# Square root of [(2 _ C _ D)/H] Following are the fixed values of C and H: C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# For example Let us assume the following comma separated input sequence is given to the program:
# 100,150,180 The output of the program should be: 18,22,24

# ---------------mine-------------
import math
# def Square_root(C, D, H):
#     temp = []
#     # for i in D:
#     #     a = round(math.sqrt((float(i)*C*2)/H))
#     #     temp.append(a)
#     temp.append(math.sqrt((i*C*2)/H) for i in D)
#     temp = ",".join(list(temp))
#     print(temp)

# C = 50
# H = 30
# D = input("Please input an integer:").split(",")
# Square_root(C, D, H)

# -------others-------
# import math
# c = 50
# h = 30
# value = []
# items = [x for x in raw_input().split(',')]
# for d in items:
#     value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

# print ','.join(value)

from math import sqrt

C,H = 50,30

def calc(D):
    return sqrt((2*C*D)/H)

D = input().split(',')                     # splits in comma position and set up in list
D = [str(round(calc(int(i)))) for i in D]  # using comprehension method. It works in order of the previous code
print(",".join(D))

