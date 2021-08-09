# String in python are surround by ether single quotation marks or double quotation marks "Hello" is the same as 'Hello'
print("Hello python") #string
print('Hello python') #There are same

a= 'this line show string method'
print(len(a))

print(a.capitalize()) # this method uppercase first letter a sentance

print(a.casefold()) # this method make the string lowercase

print(a.index('method')) # same as find() method but index()method raise an exception if the value is not found

print(a.find('string')) # this method finds the first occurrence of the specified value

print(a.count('string')) # this method show the number of times a specified value appears in the string

print(a.center(200)) # this method wil center aling the string

myTuple = ('rock', 'joker', 'not found') 
print('*#'.join(myTuple)) #join all items in a tuple into a  string using a hash or star characters as separator

print(a.replace("this line show string method", 'I love myself')) # this method replace a specified phrase with another specified phrase

print(a.split()) # this method splits a string into a list

print(a.title()) # make first letter in each word uppercase
b = 'i practics python string method \n this is a new line \n show this line a list'
print(b.splitlines())

print(a.isidentifier()) # check if the string valid indentifier

print(a.translate(b)) # translate line and word 83(s) with 80(p) {83: 80}




