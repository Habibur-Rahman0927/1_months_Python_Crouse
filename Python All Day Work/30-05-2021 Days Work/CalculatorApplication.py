# Make a calculator python program 

# def add(a,b):
#     result= a+b
#     print("a+b = ",result)
# def sub(a,b):
#     result= a-b
#     print("a-b = ",result)
# def mul(a,b):
#     result = a*b
#     print("a*b = ",result)
# def div(a,b):
#     result = a/b
#     print("a/b = ",result)

# a = int(input("Enter the first number : "))
# b = int(input("Enter the second number : "))
# oparator = input("Enter the operator : ")

# if oparator == "+":
#     add(a,b)
# elif oparator == "-":
#     sub(a,b)
# elif oparator == "*":
#     mul(a,b)
# elif oparator == "/":
#     div(a,b)
# else:
#     print("Invalid Number")

class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addition(self):
        print("a + b = ",a + b)

    def subtraction(self):
        print("a - b = ",a - b)

    def multiplication(self):
        print("a * b = ",a * b)

    def division(self):
        print("a / b = ",a / b)


a = int(input("Enter first number: "))
b = int(input("Enter Second number: "))

obj = Calculator(a,b)


choice = 1
while choice != 0:
    print("0. Exit")
    print("1. ADDITION")
    print("2. SUBTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        print(obj.addition())
    elif choice == 2:
        print(obj.subtraction())
    elif choice == 3:
        print(obj.multiplication())
    elif choice == 4:
        print(obj.division())
    elif choice == 0:
        print("Exiting!")
    else:
        print("Invalid choice")
