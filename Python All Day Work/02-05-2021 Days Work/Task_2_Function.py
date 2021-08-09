#python function

def multiple(x,y=0):
    print("the value of X : ", x)
    print("the value of Y : ", y)
    return x+y

resultMulti = multiple(20,50)
print(resultMulti)

def group(*args):
    print(args)

group(1, 2, 3, 4, 5, 8)
def f(z):
    return 3*z**2-2

result = f(3)
result1 = f(5)

print(result)
print(result1)

def fun(num1, num2):
    return num1+num2
sum = fun(100,200)
print(sum)
sum1 = fun(10,20)
print(sum1)

def add(num1, num2=0):
    return num1+num2
sum4= add(100,500)
sum3= add(100)
print(sum3)
print(sum4)

def my_f():
    print("hello from a funcition")

my_f()  

def myf(*kids):
    print('the yongest child is ' + kids[2])

myf("email", "tobias", "Linus")

def add_two_values(firstName, lastName):
    return firstName + ' ' + lastName


print(add_two_values(lastName='Habbib', firstName='Rakib'))


def addnumber():
    a = 10
    b = 10
    result = a + b
    print(result)
    return result


result = addnumber() 

def my_name():
    print("habib")


# x = 0
# def output():
#     x=1
#     def inner():
#         nonlocal x
#         x = 2
#         print("inner: ", x)|
#     inner()
#     print("outer : ", x)

# outer()

# print("globle : ", x)



def fib(n):
    a,b = 0,1
    while a<n:
        print(a,end='')
        a,b = b, a+b
    print()

fib(200)
fib(2000)
# fib
# f=fib
# f(200)

def fib2(n):
    result = []
    a,b = 0, 1
    while a<n:
        result.append(a)
        a,b = b, a+b
    return result
fibo = fib2(100)
print(fibo)

def ask_ok(prompt, retries=4,reminder='please try agin!'):
    while True:
        ok = input(prompt)
    if ok in('y', 'ye', 'yes'):
        return True
    if ok in('n', 'no', 'nop', 'nope'):
        return False
    retries = retries -1
    if retries <0:
        raise ValueError('invalid user reponse')
    print(reminder)

i = 5 
def f(arg = i):
    print(arg)
i = 6
f()

def f(a, L = []):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

def f(a,L = None):
    if L is None:
        L = []
    L.append(a)
    return L

# def count(num):
#     print(num)
#     num += 1
#     count(num)

# count(1)

# def parrot(voltage,state='a stiff', action='voom', type='Norwegian Blue'):
#     print('this parrot would', action, end='')
#     print('if you put',voltage, 'voltage through it')
#     print('lovely plumage. the', type)
#     print('its ', state)

# def f(ham:str, eggs: str ="aggs")->str:
#     print('annotations', f.__annotations__)
#     print('arguments', ham, aggs)
#     return ham + 'and' + aggs
# f('spam')