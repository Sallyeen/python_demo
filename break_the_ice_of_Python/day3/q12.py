# Write a program, which will find all such numbers between 1000 and 3000 (both included) 
# such that each digit of the number is an even number.The numbers obtained should be printed 
# in a comma-separated sequence on a single line.

# ---------------mine第一次，未理解题意，不对-------------
ans = []
for i in range(2000, 2889):
    a = i % 10
    if a % 2 != 0:
        continue
    b = i // 10 % 10
    c = i // 100 % 10
    d = i // 1000
    if b % 2 == 0 and c % 2 == 0 and d % 2 == 0:
        ans.append(str(i))
result = ",".join(ans)
print(result)

