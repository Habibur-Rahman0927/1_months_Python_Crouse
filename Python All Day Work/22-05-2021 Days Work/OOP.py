#Python oop
#Syntax 
#class YourClassName:
#       <statement-1>
#           .
#       <statement-N>
#Properties of class-
#class YourClassName:
#       '''Docstring'''
#       #Attributes - Variables
#       #Behavious - Methods(Functions)

""" class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person_1 = Person('Habib', 22)
# print(person_1)
print(person_1.name)
print(person_1.age)

class Person_A:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is  " +self.name)

person_2 = Person_A("Rasel", 36)
person_2.myfunc() """

""" class Person_B:
    def __init__(self, name, age):
        self.name = name
        self.age  = age
    def myfunc(self):
        print("Hello my name is " + self.name)


person_3 = Person_B("Aslam ", 38)
person_3.age=40
print(person_3.age)
person_3.myfunc()

class Dog:

    kind = 'canine'     

    def __init__(self, name):
        self.name = name 
d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)
print(e.kind) """

""" class Dog:
    tricks = []

    def __init__(self, name):
        self.name = name
    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)

 """

#inside the function
""" class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []  

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
print(e.tricks) """

#Random Remarks
""" class Warehouse:
    purpose = 'storage'
    region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region)
w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
x = 5
print(x) """

""" class Person:
    age = 10

    def greet(self):
        print('Hello')

harry = Person()
print(Person.greet)
print(harry.greet)
harry.greet()

class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def get_data(self):
        print(f'{self.real}+{self.imag}j')

num1 = ComplexNumber(2, 3)
num1.get_data()
num2 = ComplexNumber(5)
print((num2.real, num2.imag))
print(num1) """