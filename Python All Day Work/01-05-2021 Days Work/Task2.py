# for loop


fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)

for x in 'banna':
    print(x)

for x in fruits:
    print(x)
    if x == 'banana':
        break

for x in range(6):
    print(x)

for x in range(2, 30, 3):
    print(x)


for x in range(0, 21):
    print(x)

for x in range(2, 20, 2):
    print(x)
for x in range(1, 20, 2):
    print(x)



#for in dist


thisdict = {
    "brand" : "ford",
    "model" : "Mustang",
    "year" : 1955
}

for x in thisdict:
    print(x)


for x in thisdict.values():
    print(x)

for x, y in thisdict.items():
    print(x,y)

for key in thisdict:
    print(key, 'correspond to ', thisdict[key])


# for loop sets


thisset = { 'apple', 'banana', 'cherry'}
for x in thisset:
    print(x)

print("banana" in thisset)

num_set = [0, 1, 2, 3, 4, 5]
for n in num_set:
    print(n)

#tuple


thistuple = ('apple', 'banana', 'cherry')
for x in thistuple:
    print(x)


x = [(1, 2), (3, 4), (5, 6)]
for item in x:
    print(item)
    print(item[0])

for x in range(1, 10):
    print(x)