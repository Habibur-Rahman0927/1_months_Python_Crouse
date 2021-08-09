#nested for loop
adj = ['red', 'big', 'tasty']
furits = ['apple', 'banana', 'cherry']

for x in adj:
    for y in furits:
        print(x, y)
        print(x + ' big apple ' + y)



furits = ['apple', 'banana', 'cherry']
for x in furits:
    print(x)
    if x == "banana":
        break


for x in furits:
    if x == 'banana':
        break
    print(x)


for x in furits:
    if x == 'banana':
        continue
    print(x)



for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished")

#nested while loop

i = 1 
while i <6:
    print(i)
    if (i==3):
        break
    i+=1

a = 10
while(a>0):
    print(a)
    a-=1
    if a==1:
        break
else:
    print("reach 0")

i = 0 
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


i = 1 
while i < 6:
    print(i)
    i +=1
else: 
    print('i is no longer than less than 6')