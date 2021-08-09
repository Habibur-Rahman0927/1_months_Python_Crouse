
# 4. Polymorphism
# -------------------
# => Polymorphism is taken from the Greek words Poly (many) and morphism (forms). 
# It means that the same function name can be used for different types. 
# This makes programming more intuitive and easier.



class Calculator:
    """ Do add and sub """

    def add(self, a, b):
        print(a+b)

    def sub(self, a, b):
        print(a-b)


class Calculator_2(Calculator):
    """ Docstring """

    def division(self, a , b):
        print(a/b)

    def add(self, a, b, c):
        print(a+b+c)


class Calculator_3(Calculator_2):
    """ Do Multiplication """

    def multiplication(self, a, b):
        print(a*b)

    def add(self, a, b, c, d):
        print(a+b+c+d)


my_calculator = Calculator()
my_calculator.add(2, 2)

my_calculator_2 = Calculator_2()
my_calculator_2.add(2, 2, 2)

my_calculator_3 = Calculator_3()
my_calculator_3.add(2, 2, 2, 2)


class Rectangle:
    def __init__(self, length, breadth):
        self.l = length
        self.b = breadth

    def area(self):
        return self.l * self.b

class Square:
    def __init__(self, side):
        self.s = side

    def area(self):
        return self.s ** 2

rec = Rectangle(10, 20)
squ = Square(10)

print("Area of rectangle is: ", rec.area())
print("Area of square is: ", squ.area())

class Tomato(): 
     def type(self): 
       print("Vegetable") 
     def color(self):
       print("Red") 
class Apple(): 
     def type(self): 
       print("Fruit") 
     def color(self): 
       print("Red") 
      
def func(obj): 
       obj.type() 
       obj.color()
        
obj_tomato = Tomato() 
obj_apple = Apple() 
func(obj_tomato) 
func(obj_apple)

