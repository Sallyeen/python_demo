# Define a class with a generator which can iterate the numbers, which are divisible by 7, 
# between a given range 0 and n. Suppose the following input is supplied to the program: 7
# Then, the output should be: 0 7 14

# class divisible_7():
#     def find_num(self, n):
#         ans = ''
#         for i in range(n+1):
#             if i % 7 == 0:
#                 ans += str(i) + " "
#         return ans

# n = int(input("Please input a range:"))
# inst = divisible_7()
# ans = inst.find_num(n)
# print(ans)

# '''Solution by: ShalomPrinz
# '''
# class MyGen():
#     def by_seven(self, n):
#         for i in range(0, int(n/7) + 1):
#             yield i * 7

# for i in MyGen().by_seven( int(input('Please enter a number... ')) ):
#     print(i)

'''Solution by: Seawolf159
'''
class Divisible:

    def by_seven(self, n):
        for number in range(1,n + 1):
            if number % 7 == 0: yield number


divisible = Divisible()
generator = divisible.by_seven(int(input("Please insert a number. --> ")))
for number in generator:
    print(number)
