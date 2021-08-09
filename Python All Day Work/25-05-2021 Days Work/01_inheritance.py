# # 1. Inheritance
# # ---------------
# # => Child classes inherit data and behaviours from parent class.

class Calculator:
    def addition(self, num1, num2):
        return num1 + num2
    def subtraction(self, num1, num2):
        return num1 - num2
    def multiplication(self, num1, num2):
        return num1 * num2
    def division(self, num1, num2):
        return num1 // num2

my_calculator = Calculator()
print(my_calculator.addition(2, 3))
print(my_calculator.subtraction(5, 3))


class AdvancedCalculator:
    def addition(self, num1, num2):
        return num1 + num2
    def subtraction(self, num1, num2):
        return num1 - num2
    def multiplication(self, num1, num2):
        return num1 * num2
    def division(self, num1, num2):
        return num1 // num2
    def square(self, num):
        return num * num
    def cube(self, num):
        num * num * num

class AdvancedCalculator(Calculator):
    def square(self, num):
        return num * num
    def cube(self, num):
        return num * num * num


my_advance_calculator = AdvancedCalculator()
print(my_advance_calculator.square(2))
print(my_advance_calculator.cube(2))
print(my_advance_calculator.addition(10, 10))

class Calculator:
    def add(self, num1, num2):
        return num1 + num2
    def sub(self, num1, num2):
        return num1 - num2

my_calculator = Calculator()
print(my_calculator.add(10, 10))


class AdvancedCalculator(Calculator):    
    def cube(self, num):
        return num * num * num
    def add(self, num1, num2, num3):
        return num1 + num2 + num3

my_advance_calculator = AdvancedCalculator()
print(my_advance_calculator.add(10, 10,20))

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Aslam", "khan")
x.printname()


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Rakib", "Hero")
x.printname()

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

x = Student("First", "Needed")
x.printname()
print(x.graduationyear)

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Other", "pass data", 2019)
x.printname()
print(x.graduationyear)

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Habib", "rs", 2019)
x.welcome()
