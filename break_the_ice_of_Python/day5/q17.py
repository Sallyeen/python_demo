# Write a program that computes the net amount of a bank account based a transaction log from console 
# input. The transaction log format is shown as following: D 100 W 200 D means deposit while W means 
# withdrawal. Suppose the following input is supplied to the program: D 300 D 300 W 200 D 100 
# Then, the output should be: 500

# seq = input("Please input a sequence: ").split(" ")
# ans = 0
# for i in range(len(seq)):
#     if seq[i] == 'D':
#         ans = ans + int(seq[i+1])
#     if seq[i] == 'W':
#         ans = ans - int(seq[i+1])
# print(ans)

ans = 0
while True:
    seq = input("Please input a sequence: ")
    lst = seq.split(" ")
    if not seq:
        break
    if lst[0] == 'D':
        ans = ans + int(lst[1])
    elif lst[0] == 'W':
        ans = ans - int(lst[1])
print(ans)
