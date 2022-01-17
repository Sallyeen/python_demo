# Write a Python program that accepts a string and calculate the number of digits and letters.
# Input Hello321Bye360 Output Digit - 6 Letter - 8

seq = input("Input:")
num_dig, num_al = 0, 0
for i in seq:
    if i.isdigit():
        num_dig += 1
    if i.isalpha():
        num_al += 1
print("Digit - ", num_dig, "\nLetter - ", num_al)