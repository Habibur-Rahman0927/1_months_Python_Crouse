"""
Syntax:
class Pencil:
    <statement-1>
    .
    .
    .
    <statement-N>

Properties of class:
class ClassName:
    ''' This class or design help us to create a pencil '''
    Attributes - Variables
    Behabiours - Methods (Functions)


Pillar of OOP:
- Class & Object - Discussion topic
- Abstruction - Private and Public
- Encapsulation
- Polymorphism
- Inheritance

"""

# # Design/Class for Pencil Object
# class Pencil:
#     """ This class is designed for creating pens """
#     # Attributes - Variables
#     name = ''
#     color = ''
#     size = 0
#     model = ''

#     # Methods
#     def write(self):
#         print('Writting something by this pencil is done!')

#     def erase(self):
#         print('Erased!')

#     def details(self):
#         print('%s\n%s\n%s\n%d' % (self.name, self.model, self.color, self.size))

# # Creating Pencils Objects
# pencil_1 = Pencil()
# pencil_1.name = 'Matador Pluto'
# pencil_1.color = 'Blue'
# pencil_1.size = 5
# pencil_1.model = 'HB'
# pencil_1.details()


# class Pen:
#     """ This class is designed for creating pen """
 
#     name = ''
#     color = ''
#     model = ''

#     def write(self):
#         print('Writting something by this pen is done!')

#     def erase(self):
#         print('Erased!')

#     def details(self):
#         print('%s\n%s\n%s' % (self.name, self.model, self.color))

# pen_1 = Pen()
# pen_1.name = 'Matador Pinpoint'
# pen_1.color = 'green'
# pen_1.model = 'Bolpen'
# pen_1.details()

# class Dog:
#     def __init__(self, name, age):  
#         self.name = name
#         self.age = age

#     def bark(self):
#         print("bark bark!")

#     def doginfo(self):
#         print(self.name + " is " + str(self.age) + " years old.")

# ozzy = Dog("Ozzy", 2)
# ozzy.doginfo()
# skippy = Dog("Skippy", 12)
# skippy.doginfo()
# filou = Dog("Filou", 8)
# filou.doginfo()

# class Dog:

#     def __init__(self, name, age):  
#         self.name = name
#         self.age = age

#     def bark(self):
#         print("bark bark!")

#     def doginfo(self):
#         print(self.name + " is " + str(self.age) + " year(s) old.")

#     def birthday(self):
#         self.age +=1


# ozzy = Dog("Ozzy", 2)
# print(ozzy.age)
# ozzy.birthday()
# print(ozzy.age)
# ozzy.birthday()
# print(ozzy.age)


# class Dog:

#     def __init__(self, name, age):  
#         self.name = name
#         self.age = age

#     def bark(self):
#         print("bark bark!")

#     def doginfo(self):
#         print(self.name + " is " + str(self.age) + " year(s) old.")

#     def birthday(self):
#         self.age +=1

#     def setBuddy(self, buddy):
#         self.buddy = buddy
#         buddy.buddy = self

# ozzy = Dog("Ozzy", 2)
# filou = Dog("Filou", 8)

# ozzy.setBuddy(filou)

# print(ozzy.buddy.name)
# print(ozzy.buddy.age)

# print(filou.buddy.name)
# print(filou.buddy.age)

# class Snake:

#     def __init__(self, name):
#         self.name = name

#     def change_name(self, new_name):
#         self.name = new_name

# python = Snake("python")
# anaconda = Snake("anaconda")

# print(python.name)
# python
# print(anaconda.name)
# anaconda

#our cls practice

class Pencil:

    model = '2B' 

    def __init__(self):
        self.name = 'Matador'
        self.color = 'Blue'
        
    def details(self):
        pass

pencil_1 = Pencil()
pencil_2 = Pencil()
pencil_3 = Pencil()
pencil_4 = Pencil()

Pencil.model = '4B'
print(pencil_4.name, pencil_4.color[3], pencil_4.model)
print(pencil_1.name, pencil_1.color[2], pencil_1.model)
#pencil_2.color = 'Yellow'
print(pencil_2.name, pencil_2.color[1], pencil_2.model)
print(pencil_3.name, pencil_3.color[0], pencil_3.model)

