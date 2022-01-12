# Write a program to compute the frequency of the words from the input. The output should output after 
# sorting the key alphanumerically. Suppose the following input is supplied to the program: New to 
# Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3。 Then, the output should be:
# 2:2 3.:1 3?:1 New:1 Python:5 Read:1 and:1 between:1 choosing:1 or:2 to:1

# fre = {}
# seq = input("Please input: ").split()
# for item in seq:
#     fre[item] = fre.get(item, 1)

# words = fre.keys
# words.sort()
# ans = ''
# for key in words:
#     print(key, ': ', seq[key])

ss = input().split()
word = sorted(set(ss))     # split words are stored and sorted as a set

for i in word:
    print("{0}:{1}".format(i,ss.count(i)))