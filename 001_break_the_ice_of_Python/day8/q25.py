# Define a class, which have a class parameter and have a same instance parameter.

# ---------------法一------------------
# class Person:
#     name = 'Person'

#     def __init__(self, name = None):
#         self.name = name

# David = Person('David')
# print(David.name)

# sam = Person()
# print(sam.name)
# sam.name = 'sam'
# print(sam.name)

# ------------------法二-----------------
class Car:
    name = "Car"

    def __init__(self,name = None):
        self.name = name

honda=Car("Honda")
print("%s name is %s"%(Car.name,honda.name))

toyota=Car()
toyota.name="Toyota"
print("%s name is %s"%(Car.name,toyota.name))