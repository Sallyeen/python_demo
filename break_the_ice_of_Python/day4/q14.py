# Write a program that accepts a sentence and calculate the number of letters and digits. 
# Suppose the following input is supplied to the program: hello world! 123 Then, the output should be:
# LETTERS 10 DIGITS 3

# ---------------mine第一次，未理解题意，不对-------------
n = input("Please input an integer: ")
count_l = 0
count_d = 0
for i in n:
    if i.isalpha():
        count_l += 1
    if i.isdigit():
        count_d += 1
print("LETTERS", count_l, "DIGITS", count_d)


