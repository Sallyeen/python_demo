# Define a class named American which has a static method called printNationality.
# 静态方法是不管是否被实例化，都可直接通过类名调用

class American():
    @staticmethod
    def printNationality():
        print("The nationality of American is American.")

American.printNationality()

american = American()
american.printNationality()