# Define a class which has at least two methods: getString: to get a string from console input 
# printString: to print the string in upper case. Also please include simple test function to 
# test the class methods.

# ---------------mine，好像有些怪，但是无误-------------
# class Q5():
#     def getString(self):
#         n = input("Please input a string:")
#         return n
#     def printString(self):
#         getstring = self.getString()
#         print(getstring.upper())
#         return
# q5 = Q5()
# q5.printString()

# offical
class IOstring():
    def get_string(self):
        self.s = input()

    def print_string(self):
        print(self.s.upper())

xx = IOstring()
xx.get_string()
xx.print_string()

# others
# class InputOutString(object):
#     def __init__(self):
#         self.s = ""

#     def get_string(self):
#         self.s = input()

#     def print_string(self):
#         print(self.s.upper())

# str_obj = InputOutString()
# str_obj.get_string()
# str_obj.print_string()



