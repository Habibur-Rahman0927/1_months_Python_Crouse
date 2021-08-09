# Errors and Exception Handling

"""
FileNotFoundError
ImportError
IndentationError
IndexError
KeyboardInterrupt
KeyError
OSError
NameError
SyntaxError
RuntimeError
SystemError
StopIteration
TabError
TypeError
UnboundLocalError
ValueError
WindowError
ZeroDivisionError
"""

# with open('test.txt', mode='r') as my_file:
#     content = my_file.read()
#     print(content)

# print('Hello, I am Fine.')


# Exception Handling
"""
try:
    your code
except:
    message
"""

# try:
#     with open('test.txt', mode='r') as my_file:
#         data = my_file.read()
#         print(data)
# except:
#     print("Oops!! File Not Found.")

# print('Hello, Its working')

"""
try:
    your code
except ExceptionName:
    your message
"""

# try:
#     with open('test.txt', mode='r') as my_file:
#         data = my_files.read()
#         print(data)
# except NameError:
#     print('Name not found')

# print('Hello, Its working.')

"""
try:
    your code
except ExceptionName1:
    message
except ExceptionName2:
    message
"""

# try:
#     with open('test.txt', mode='r') as my_file:
#         data = my_file.read()
#         print(data)
# except NameError:
#     print('Name not found')
# except FileNotFoundError:
#     print('Oops!!, File not found.')

# print('Hello, Its working.')


"""
try:
    your code
except (ExceptionName1, ExceptionName2...)
    message
"""

# try:
#     with open('test.txt', mode='r') as my_file:
#         data = my_file.read()
#         print(data)
# except (NameError, FileNotFoundError):
#     print('Errors Found! Please check')

# print('Hello, Its working.')


"""
try:
    your code
except ExceptionName as msg:
    msg
"""

# with open('test.txt', mode='r') as my_file:
#         print('Yes')
#         data = my_file.read()
#         print(data)

# try:
#     with open('test.txt', mode='r') as my_file:
#         print('Yes')
#         data = my_file.read()
#         print(data)
# except FileNotFoundError as msg:
#     print(msg)
#     print('Please ensure that required file is exist')

# print('Hello, Its working.')

"""
try:
    your code
except ExceptionName:
    message
else:
    message
"""

# try:
#     with open('test.txt', mode='r') as my_file:
#             data = my_file.read()
#             print(data)
# except FileNotFoundError:
#     print("Oops!! File not found.")
# else:
#     print('No errors found :)')

# print('Hello, Its working.')

"""
try:
    your code
except ExceptionName:
    message
else:
    message
finally:
    your code
"""

# try:
#     with open('test.txt', mode='r') as my_file:
#             data = my_file.read()
#             print(data)
# except FileNotFoundError:
#     print("Oops!! File not found.")
# else:
#     print('No errors found :)')
# finally:
#     print('Finally')
#     my_file.close()

# print('Hello, Its working.')


"""
try:
    raise NameError('Hello, It is user defined error msg.')
except NameError as msg:
    message
"""

# try:
#     raise NameError('Hello, It is user defined error msg.')
# except NameError as msg:
#     print(msg)