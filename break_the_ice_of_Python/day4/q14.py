# Write a program that accepts a sentence and calculate the number of upper case letters and lower case 
# letters. Suppose the following input is supplied to the program: Hello world! Then, the output should be:
# UPPER CASE 1 LOWER CASE 9

# ---------------mine第一次，未理解题意，不对-------------
seq = input("Please input an integer: ")
count_upper, count_lower = 0, 0
for i in seq:
    if not i.isalpha():
        continue
    if i.isupper():
        count_upper += 1
    elif i.islower():
        count_lower += 1
print("UPPER CASE %d LOWER CASE %d" % (count_upper, count_lower))

