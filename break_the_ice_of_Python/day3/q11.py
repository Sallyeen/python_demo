# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input 
# and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are 
# to be printed in a comma separated sequence. Example: 0100,0011,1010,1001 Then the output should be:
# 1010 Notes: Assume the data is input by console.

# ---------------mine第一次，未理解题意，不对-------------
n = input("Please input an integer: ").split(",")
for i in n:
    ans = int(i, 2)
    if ans % 5 == 0:
        print(i)


