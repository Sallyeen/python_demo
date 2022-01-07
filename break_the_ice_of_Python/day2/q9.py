# Write a program that accepts sequence of lines as input and prints the lines after making 
# all characters in the sentence capitalized. Suppose the following input is supplied to the program:
# Hello world Practice makes perfect Then, the output should be:
# HELLO WORLD PRACTICE MAKES PERFECT

# ---------------mine第一次，未理解题意，不对-------------
# n = input("Please input an integer: ")
# print(n.upper())

# ---------------mine-------------
# line = str()
# while True:
#     n = input("Please input an sentence: ")
#     if n:
#         line += n
#     else:
#         break
# print(line.upper())

# ---------------others
# line = list()
# while True:
#     n = input("Please input an sentence: ")
#     if n:
#         line.append(n.upper())
#     else:
#         break
# for item in line:
#     print(item)

def inputs():
    while True:
        string = input()
        if not string:
            return
        yield string

print(*(line.upper() for line in inputs()),sep='\n')

