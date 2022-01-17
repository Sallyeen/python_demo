# You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form 
# of Indian folk art based on creation of patterns.) Different sizes of alphabet rangoli are shown below:
#size 3
# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----
#size 5  4(n-1)+1=4n-3;2(n-1)+1=2n-1
# --------e--------0
# ------e-d-e------1
# ----e-d-c-d-e----2
# --e-d-c-b-c-d-e--3
# e-d-c-b-a-b-c-d-e4
# --e-d-c-b-c-d-e--5
# ----e-d-c-d-e----6
# ------e-d-e------7
# --------e--------8


def rangoli(n):
    # your code goes here
    l1=list(map(chr,range(97,123)))
    x=l1[n-1::-1]+l1[1:n]
    mid=len('-'.join(x))
    for i in range(1,n):
        print('-'.join(l1[n-1:n-i:-1]+l1[n-i:n]).center(mid,'-'))
    for i in range(n,0,-1):
        print('-'.join(l1[n-1:n-i:-1]+l1[n-i:n]).center(mid,'-')) 
rangoli(5)

