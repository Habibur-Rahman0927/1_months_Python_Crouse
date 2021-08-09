

# -------------------
# 1. Encapsulation 
# -------------------
# => containing information in an object, 
# exposing only selected information.

# Python uses three types of access modifiers;
# they are - 
# 1. Public
# 2. Private
# 3. Protected

# Need for encapsulation in Python:
#     * Encapsulation helps to achieve well-defined, readable code.
#     * Users can securely maintain the applications.
#     * Encapsulation ensures the code’s simplicity and flexibility through proper code organization 
#       and assists with a smooth user experience.


class Calculator:
    name = 'Public Properties'
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        print(self.a + self.b)

my_calculator = Calculator(5, 5)
my_calculator.add()
print(my_calculator.name)


# # 2. Protected

# Protected members are accessible within the class and also available to its sub-classes. 
# To define a protected member, prefix the member name with a single underscore “_”.

class Student:
    def __init__(self, name, roll, address):
        self.name = name
        self.roll = roll
        self._address = address

    def _profile(self):
        print(self.name, self.roll, self._address)

my_student = Student('Forid', 20, 'Mirpur')
print(my_student._address)
my_student._profile()



# 2. Private

# Private members are accessible within the class. 
# To define a private member, prefix the member name with a double underscore “__”.

class Student:
    def __init__(self, name, roll, address):
        # Public
        self.name = name
        # Protected
        self._address = address
        # Private
        self.__roll = roll

    def __profile(self):
        print(self.name, self.__roll, self._address)


my_student = Student('Forid', 20, 'Banani')
print(my_student.name)
print(my_student._address)
# print(my_student.__roll)

# Access mechanism
print(my_student._Student__roll)


class Person:
  def __init__(self, name, age=0):
    self.name = name
    self.age = age

  def display(self):
    print(self.name)
    print(self.age)

person = Person('Hello', 40)
#accessing using class method
person.display()
#accessing directly from outside
print(person.name)
print(person.age)


class Person:
  def __init__(self, name, age=0):
    self.name = name
    self.__age = age

  def display(self):
    print(self.name)
    print(self.__age)

  def getAge(self):
    print(self.__age)

  def setAge(self, age):
    self.__age = age

person = Person('setage anthor', 40)
#accessing using class method
person.display()
#changing age using setter
person.setAge(45)
person.getAge()

class edpresso:
    def __init__(self, name, project):
        self._name = name
        self._project = project

edp = edpresso("TeamPhoenix", 2)

print("Name:",edp._name)
print("project:",edp._project)


class edpresso:
   def __init__(self, name, project):
      self.name = name
      self.__project = project
edp = edpresso('TeamPhoenix', 3)
print("Name:",edp.name)

print("Project:",edp._edpresso__project)

# class Car:

#     def __init__(self):
#         self.__updateSoftware()

#     def drive(self):
#         print('driving')

#     def __updateSoftware(self):
#         print('updating software')

# redcar = Car()
# redcar.drive()

# class Car:

#     __maxspeed = 0
#     __name = ""
    
#     def __init__(self):
#         self.__maxspeed = 200
#         self.__name = "Supercar"
    
#     def drive(self):
#         print('driving. maxspeed ' + str(self.__maxspeed))

# redcar = Car()
# redcar.drive()
# redcar.__maxspeed = 10
# redcar.drive()