# Define a class named Shape and its subclass Square. The Square class has an init function 
# which takes a length as argument. Both classes have a area function which can print the area 
# of the shape where Shape's area is 0 by default.
# class Shape():
#     def __init__(self, ar=0):
#         self.ar = ar
#     def area(self):
#         print(self.ar)

# class Square(Shape):
#     def __init__(self, ar, l):
#         self.ar = ar
#         self.length = l
#     def area(self):
#         print(self.ar)
        
# shape = Shape()
# shape.area()
# square = Square(3, 2)
# square.area()

class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self,length = 0):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length*self.length

Asqr = Square(5)
print(Asqr.area())      # prints 25 as given argument

print(Square().area())  # prints zero as default area

