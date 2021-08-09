# sets are used to store multiple items in a single variable
my_set = {'Hero', 1, 'nothing', 'rock'}
print(my_set)
print(type(my_set))

# make  set from a list
my_set1 = set(['Hero', 1, 'nothing', 'rock']) 
print(my_set1)

#initialize set
myset = {} 
print(myset)
print(type(myset))

a = set()
print(a)
print(type(a))

# set Modify

my_new_set = {1, 3}
print(my_new_set)

# add element
my_new_set.add(2) 
print(my_new_set)

# add multiple element
my_new_set.update([4, 5, 6]) 
print(my_new_set)

# add list and set
my_new_set.update([4, 9], {1, 2, 3}) 
print(my_new_set)

# deffernce between discard() and remove

#discard 9
my_new_set.discard(9) 
print(my_new_set)

my_new_set.remove(2)
print(my_new_set)

A = {1, 2, 3, 4}
B = {5, 4, 1, 8}
print(A-B)
print('return value is ', A.pop())

print('A = ', A)