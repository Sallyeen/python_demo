# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, 
# DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
# UP 5 DOWN 3 LEFT 3 RIGHT 2 The numbers after the direction are steps. Please write a program to 
# compute the distance from current position after a sequence of movement and original point. 
# If the distance is a float, then just print the nearest integer. Example: If the following tuples 
# are given as input to the program: UP 5 DOWN 3 LEFT 3 RIGHT 2 Then, the output of the program 
# should be: 2

import math

n1, n2 = 0, 0
while True:
    seq = input("Please input:").split()
    print(seq)
    # seqq = input("Please input:").split(" ")                  ['']
    # seqeq = input("Please input:").split(' ')                 ['']
    if not seq:
        break
    if seq[0] == 'UP':
        n1 += int(seq[1])
    elif seq[0] == 'DOWN':
        n1 -= int(seq[1])
    elif seq[0] == 'LEFT':
        n2 += int(seq[1])
    elif seq[0] == 'RIGHT':
        n2 -= int(seq[1])
ans = round(math.sqrt(n1 ** 2 + n2 ** 2))
print(ans)

# import  math

# x,y = 0,0
# while True:
#     s = input().split()
#     if not s:
#         break
#     if s[0]=='UP':                  # s[0] indicates command
#         x-=int(s[1])                # s[1] indicates unit of move
#     if s[0]=='DOWN':
#         x+=int(s[1])
#     if s[0]=='LEFT':
#         y-=int(s[1])
#     if s[0]=='RIGHT':
#         y+=int(s[1])
#                                     # N**P means N^P
# dist = round(math.sqrt(x**2 + y**2))  # euclidean distance = square root of (x^2+y^2) and rounding it to nearest integer
# print(dist)
        
