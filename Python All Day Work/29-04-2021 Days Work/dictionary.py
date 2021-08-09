# Dictionaries are used to store data values in key : value paris

thisdict = {
    "brand" : "Ford",
    "Model" : "Mustang",
    "year" : 1964
}
print(thisdict)
print(type(thisdict))
print(thisdict["Model"])
print(len(thisdict))

my_dict = {}
print(my_dict)
my_dict1 = {1: 'hero', 2: 'zero'} # dictionary with integer keys
print(my_dict1)

my_dict2 = dict([(1, 'apple'), (2, 'banana')]) # from sequence having each item as a pair
print(my_dict2)

my_dict3 = {'name' : 'rockstar','Home' : 'Gazipur', 'age' : '35'}
my_dict3['age'] = 22 #modify
print(my_dict3)

my_dict3['Home'] = 'Dhaka'
print(my_dict3)

print(my_dict3.keys())
my_dict3.clear()
print(my_dict3)