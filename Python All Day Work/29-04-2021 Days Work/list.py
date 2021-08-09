# python list 
my_list = [] # empty list
print(my_list)

my_list1 = [1, 2, 3] # list of intgers
print(my_list1)

my_list2 = [1, 'Hello', 3.5] #list with mixed data type
print(my_list2)

my_list3 = ['Hero', [1, 2, 3], ['a'], 'rock'] # nested list
print(my_list3)

#list indexing
my_list4 = ['Hero', 'zero', 'nothing']
print(my_list4[0])

my_list5 = ['H', 'e', 'r', 'o']
print(my_list5[3])

#nested list indexing
my_list6 = ['Happy', [2,4,1,4],'Boring']
print(my_list6[0][1])

#Negitive indexing in lists 
my_list7 = ['H', 'E', 'R', 'O']
print(my_list7[-1])
print(my_list7[-4])

#list slicing 
my_list8 = ['p', 'r', 'o', 'g', 'r', 'a', 'm']
print(my_list8[2:5]) # list elements 3rd to 5th
print(my_list8[-5]) # elements begining to 4th
print(my_list8[5:]) # elements 6th to end
print(my_list8[:]) # elements first to end


#correcting mistake values in a list
odd = [2, 5, 56]
odd[0] = 1 # change list item
print(odd)
odd[1:3] = [5, 6, 9] # change 2nd to 3rd
print(odd)

#Appending and Extending lists
odd.append(10)
print(odd)

odd.extend([9, 41, 8])
print(odd)

#concatenating and repating list
print(odd + [5, 8, 6])
print(["re"] * 9)
 
# deleting list item
del my_list8[2]
print(my_list8)

print(my_list8.pop(1))
my_list8.clear() #list clear
print(my_list8)
my_list7.reverse()
print(my_list7) # list reverse

old_list = [1, 2, 3]
print(old_list)
new_list = old_list
new_list.append('a')
print('new list', new_list)
print('old list', old_list)
