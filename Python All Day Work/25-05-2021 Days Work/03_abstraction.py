
# -------------------
# 2. Abstraction
# -------------------
# => It is used to hide the background details or any unnecessary implementation.
# Python by default don't support abstract class directly. 
# For doing this we need abc(abstract base class) module in python.

# => If any class has any abstract method then this class called is abstract class.



from abc import ABC, abstractmethod


class Calculator(ABC):

    @abstractmethod
    def add(self, a, b):
        pass


# my_calculator = Calculator()
# my_calculator.add(2, 3)

class Calculator_2(Calculator):
    """ Docstring """

    def addition(self, a, b):
        print(a+b)

    def add(self, a, b, c):
        print(a+b+c)

my_calculator_2 = Calculator_2()
my_calculator_2.addition(20,9)
my_calculator_2.add(10, 20, 20)


class Payment(ABC):
  def print_slip(self, amount):
    print('Purchase of amount- ', amount)
  @abstractmethod
  def payment(self, amount):
    pass

class CreditCardPayment(Payment):
  def payment(self, amount):
    print('Credit card payment of- ', amount)

class MobileWalletPayment(Payment):
  def payment(self, amount):
    print('Mobile wallet payment of- ', amount)

obj = CreditCardPayment()
obj.payment(100)
obj.print_slip(100)
print(isinstance(obj, Payment))
obj = MobileWalletPayment()
obj.payment(200)
obj.print_slip(200)
print(isinstance(obj, Payment))


class type_shape(ABC): 
  def area(self): 
    #abstract method
    pass

class Rectangle(type_shape):
  length = 6
  breadth = 4
  def area(self):
    return self.length * self.breadth

class Circle(type_shape):
  radius = 7
  def area(self):
    return 3.14 * self.radius * self.radius

class Square(type_shape):
  length = 4
  def area(self):
    return self.length*self.length

class triangle:
  length = 5
  width = 4
  def area(self):
    return 0.5 * self.length * self.width


r = Rectangle() # object created for the class 'Rectangle'
c = Circle() # object created for the class 'Circle'
s = Square() # object created for the class 'Square'
t = triangle() # object created for the class 'triangle'
print("Area of a rectangle:", r.area()) # call to 'area' method defined inside the class.
print("Area of a circle:", c.area()) # call to 'area' method defined inside the class.
print("Area of a square:", s.area()) # call to 'area' method defined inside the class.
print("Area of a triangle:", t.area()) # call to 'area' method defined inside the class.