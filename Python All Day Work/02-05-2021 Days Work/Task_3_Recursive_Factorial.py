# Factorial iterative Way
# 0! = 1 
# 1! = 0*1
# 2! = 1*2
# 3! = 1*2*3
# 4! = 1*2*3*4
# 5! = 1*2*3*4*5
# 6! = 1*2*3*4*5*6
# 7! = 1*2*3*4*5*6*7
# 8! = 1*2*3*4*5*6*7*8
# 9! = 1*2*3*4*5*6*7*8*9
# 10! = 1*2*3*4*5*6*7*8*9*10


# n = int(input('Enter the number: '))

# for i in range(1, n):
#     n = n*i
# print(n)


# Factorialnumber = int(input("Enter the number : "))
# def factorial(num):
#     if num < 0 :
#         print("sorry, Factorial does not exist for nagtive number")
#     elif num == 0:
#         print("The Factorial is 1 ")
#     else:

#         for i in range(1, num):
#             num = num*i
#             print(num)
#         print("The value of Factorial Number : ",num)
# print(factorial(Factorialnumber))


# Factorial Recursive way

# 0! = 1 
# 1! = 0*1
# 2! = 1*2
# 3! = 1*2*3
# 4! = 3!*4
# 5! = 4!*5
# 6! = 5!*6
# 7! = (7-1)!*7
# 8! = (8-1)!*8
# 9! = (9-1)!*9
# n! = (n-1)!*n
# n! = n*(n-1)



def fact(n):
    if n == 1:
        return n
    else:
        return n*fact(n-1)

num = int(input("Enter the number  : "))

if num < 0:
    print("sorry, Factorial does not exist for nagtive number")
elif num == 0:
    print("this factorial is 1")
else:
    print("The Factorial of ", num, "is", fact(num))





