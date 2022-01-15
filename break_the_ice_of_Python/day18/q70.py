# Please write a program to output a random even number between 0 and 10 inclusive using 
# random module and list comprehension.

import random

lst = [i for i in range(0, 11, 2)]
ans = random.choice(lst)
print(ans)