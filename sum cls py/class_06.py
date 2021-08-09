# num1 = num2 = 0
# result = num1 + num2
# print(result)

def function_name():
    # comment
    pass

# Calling function
function_name()

def print_my_name():
    # this function print my name
    print('Karim')

# calling print_my_name function
# print_my_name()

def service_man():
    return 'How can I help you?'

# result = service_man()
# print(result)


# def add_two_values():
#     # added two integers values
#     a = 10
#     b = 10
#     result = a + b
#     print(result)
#     return result


# result = add_two_values()  
# print('return: ', result)
# print(add_two_values() + 10)

def abrar_abirer_murgi():
    return "ANDAA OR SMALL DIM"

# print(abrar_abirer_murgi())

def add_two_values(a, b):
    return a + b

# I passing arguments through function calling
# result = add_two_values('5', '5')
# print(result)

# Required Argument
# Keyword Argument
# Default Argument
# Variable length Argument (1. non-keyword, 2.keyword)


# Required Argument
# def add_two_values(a, b, c):
#     # this function added two values
#     result = a + b + c
#     return result


# result = add_two_values(1, 2, 3)
# print(result)


# Keyword Argument
# def add_two_values(first_name, last_name):
#     return first_name + ' ' + last_name


# print(add_two_values(last_name='Karim', first_name='Mohammad'))


# Default Argument
# def add_two_values(a=0, b=0, c=5):
#     return a + b + c

# print(add_two_values())
# print(add_two_values(10, 10))


# Variable length Argument - (non-Keyword)
# def add_multiple_values(*args):
#     # args = (2, 3, 5, 10, 1, 9)
#     print(type(args))

#     result = 0

#     for number in args:
#         result = result + number
#     return result


# output = add_multiple_values(2, 3, 5, 10, 1, 9, 10, 60)
# print(output)


# Variable length Argument - (Keyword)
# def add_multiple_values(**args):
#     # args = (2, 3, 5, 10, 1, 9)
#     print(type(args))

#     result = 0

#     for key in args:
#         print(key)
#         result = result + args[key]
#     return result


# output = add_multiple_values(a=2, b=3, c=5, d=10)
# print(output)

# # lambda
# sum = lambda a, b: a + b
# print(sum(10, 20))


# # Global, Local, Nonlocal variables & Global keyword

# # Global variable
# count = 10

# def add_value():
#     # local variable
#     result = 10
#     count = 20
#     print('Local: ', count)

#     def add_values2():
#         nonlocal result
#         result = 15
#         d = 10
#         print('d: ', 10)
#         print('result: ', result)
#     add_values2()
#     print('result: ', result)


# add_value()
# print('Gloabl: ', count)

# RECURSION
# def count(num):
#     print(num)
#     num += 1
#     count(num)

# count(1)
