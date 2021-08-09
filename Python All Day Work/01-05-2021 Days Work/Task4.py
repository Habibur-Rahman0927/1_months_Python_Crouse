num = int(input('Enter the number : '))

for i in range(1,11):
    print(num, 'x', i, '=', num*i)

number = int(input('Enter any number :'))
i = 0
while i < 10 and number:
    i+= 1
    print(number, 'x', i, '=', number*i)