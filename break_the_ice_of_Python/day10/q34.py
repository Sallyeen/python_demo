# Define a function which can generate a list where the values are square of numbers between 1 and 20 
# (both included). Then the function needs to print the first 5 elements in the list.

def print_5_lst():
    ans = [i ** 2 for i in range(1, 21)]
    print(ans[0:5])

print_5_lst()