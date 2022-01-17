# You are given a string.Your task is to count the frequency of letters of the string and print the
#  letters in descending order of frequency. If the following string is given as input to the program:
# aabbbccde Then, the output of the program should be: b 3 a 2 c 2 d 1 e 1

seq = input("Input:")
ans = {i:seq.count(i) for i in seq}
print(ans)