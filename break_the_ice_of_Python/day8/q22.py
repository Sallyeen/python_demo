# Write a program to compute the frequency of the words from the input. The output should output after 
# sorting the key alphanumerically. Suppose the following input is supplied to the program: New to 
# Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3。 Then, the output should be:
# 2:2 3.:1 3?:1 New:1 Python:5 Read:1 and:1 between:1 choosing:1 or:2 to:1
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3

# -----------------法一---------------------
# ss = input().split()
# word = sorted(set(ss))     # split words are stored and sorted as a set

# for i in word:
#     print("{0}:{1}".format(i,ss.count(i)))

# -----------------法二---------------------
ss = input().split()
seq = {i:ss.count(i) for i in ss}
seq_lst = sorted(seq.keys()) #括号不能忘

for i in seq_lst:
    print('%s:%s' % (i,seq[i]))

# -----------------法三---------------------
# from pprint import pprint
# p=input().split()
# pprint({i:p.count(i) for i in p})

# -----------------法四---------------------
# from collections import Counter

# seq = input("input:").split()
# seq = Counter(seq)
# index = sorted(seq.keys())
# for i in index:
#     print('{0}:{1}'.format(i, seq[i]))
