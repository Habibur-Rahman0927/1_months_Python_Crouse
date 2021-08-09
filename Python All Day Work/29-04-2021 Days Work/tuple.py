#tuple are used  to store multiple items in a single variable

thistuple = ('apple', 1, 'banana', 'cherry')
print(thistuple)

print(len(thistuple))

print(type(thistuple))

my_tuple = 3, 4.6, 'hero'
print(my_tuple)
print(type(my_tuple))
a, b, c = my_tuple
print(a)
print(b)
print(c)

#indicate tuple

my_tuple = ('hero')
print(type(my_tuple)) #string class

my_tuple1 = ('hero',)
print(type(my_tuple1)) # this class is tuple

# Accessing tuple
my_tuple3 = ('t', 'u', 'p', 'l', 'e')
print(my_tuple3[0])
print(my_tuple3[4])

nasted_tuple = ('hero', [2, 5, 9], [8, 6, 3,])
print(nasted_tuple[1][2])

#slicing

my_tuple4 = ('t', 'u', 'p', 'l', 'e')

print(my_tuple4[1:4])
print(my_tuple4[:-4])
print(my_tuple4[2:])
print(my_tuple4[:])

