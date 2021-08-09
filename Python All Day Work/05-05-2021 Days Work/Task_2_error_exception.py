# Python Error and Exception Handling

""" 
    try: 
        your code
    except:
        message
 """



# try:
#     with open('test.txt', mode='r') as open_file:
#         openFlie = open_file.read()
#         print(data)

# except:
#     print("File is not found")

# print('Hello, its working')


"""
try:
    your code
except ExceptionName:
    your message
"""


# try:
#     with open('test.txt', mode='r') as my_new_file:
#         data_file = my_new_files.read()
#         print(data_file)
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
#     with open('test.txt', mode='r') as my_new_file:
#         data = my_new_file.read()
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




# try:
#     with open('test.txt', mode='r') as my_new_file:
#         print('Yes')
#         data = my_new_file.read()
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
#     with open('test.txt', mode='r') as my_new_file:
#             data = my_new_file.read()
#             print(data)
# except FileNotFoundError:
#     print("File not found.")
# else:
#     print('No errors found :')

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
#     with open('test.txt', mode='r') as my_new_file:
#             data = my_new_file.read()
#             print(data)
# except FileNotFoundError:
#     print(" File not found.")
# else:
#     print('No errors found :')
# finally:
#     print('Finally')

# print('Hello, Its working.')

"""
try:
    raise NameError('Hello, It is user defined error msg.')
except NameError as msg:
    message
"""



try:
    raise NameError('Hello, It is user defined error msg.')
except NameError as msg:
    print(msg)