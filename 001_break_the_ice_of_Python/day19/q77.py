# lease write a program to print the running time of execution of "1+1" for 100 times.

import time

start = time.clock()
for _ in range(100):
    ans = 1 + 1
end = time.clock()
print("The running time is: ", end-start)