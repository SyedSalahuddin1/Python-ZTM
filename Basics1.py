# # Data Types

# 1.int
# 2.float
# 3.str  immutable 
# 4.bool
# 5.list
# 6.set
# 7.dict
# 8.tuple
# 9.None
# 10.complex
# bin()

print(bin(10))
print(int('0b101', 2))

# # Classes -> Custom types

# Speacilized Data Types
# Modules 

# None

# 1
print(type(2+4))
print(2-4)
print(2 * 4)
print(type(3.5+4.7))
print(2**4)

# math functions
print(round(2.89))
print(abs(-39))

print((5 + 4) * 10 / 2)

print(((5 + 4) * 10) / 2)

print((5 + 4) * (10 / 2))

print(5 + (4 * 10) / 2)

print(5 + 4 * 10 // 2)

# # augmented assignment operator
# += 
# *=
# /=
# -=

print("Hello, This is Syed Salahuddin!")

username = "SalahCoder"

# Python Keywords
# https://www.w3schools.com/python/python_ref_keywords.asp

long_string = '''
WOW, This is Legit a Long String,
This is a whole new Experience.
'''

# String concatenations
print("Syed " + "Salahuddin")

# type conversion
print(type(str(100)))

# Escape Sequence in Python \
weather = "\t It's 'Kind of' Sunny, \n Its Crazy Kind of Cold here"
print(weather)

name = "Salahuddin"
age = 24

# Formatted Strings
# Old way was .format
print(f'Hi {name}, You are {age} years old.')

print("\tBreak")
# String indexing
# 0123456789.....
# [0:2] can be anything
# [2:]
# [:3]
# [::2] skip every n time
# [-2] reverse indexing
# [::-1] skipping in reverse
# Basically [start, stop, stepover] 


name = "I am Syed Salahuddin, Learning Python by practicing daily, I'm sure that I will practice daily"

print(name[1:4])
print(name[2:])
print(name[:])
print(name[1:100])
print(name[-1])
print(name[-4])
print(name[:-3])
print(name[-4:])
print(name[::-4])

# Built In Python Methods
# https://docs.python.org/3/library/functions.html

# Built In Python String Methods
# https://www.w3schools.com/python/python_ref_string.asp

# Booleans True or False

# Type Conversion
# birth_year = int(input("What year were you born? "))
# print(birth_year)

# age = 2026 - birth_year

# print(f"You are {age} year's old.")

# https://realpython.com/python-comments-guide/

# LISTS
# 0 based indexing
# mutable
 

li = ['a', 'b', 'c', 'd', 1, 2, 3, 4, "True", "False"]
print(li[1:])

# List Slicing
# Changing values 
# Accessing From start to end , stepover
# [start, stop, stepover]
# -ve based indexing

# MATRIX
# 2D or multi dimensional list

matrix = [
    [1, 2, 3],
    [4, 5, 6], 
    [7, 8, 9]
]

print(matrix[1][2])

# List Methods
# Python List Methods
# https://www.w3schools.com/python/python_ref_list.asp

numerics = [1, 2, 3, 4, 5]

numerics.append(6)
print(numerics)

new_list = numerics
print(new_list)

# adding
new_list.insert(2, 100)
print(new_list)

new_list.extend([102, 103])
print(new_list)

# removing
# returns or removes something depending on variable names
new_list.pop() #index can also be used
print(new_list)

new_list.remove(2)
print(new_list)

# new_list.clear()
# print(new_list)

print(new_list.index(3))

alpha = ['a', 'b','x','q', 'c', 'd', 'e']
# print(alpha.index('d', 0, 4))
print('d' in alpha)
print('x' in alpha)
print(sorted(alpha)) #doesn't modify basket just makes a copy

ap = alpha.copy()
ap.reverse()
print(ap)
print(alpha[::-1])

print(list(range(1, 100, 10)))

# sentence = ' '
n_sentence = ' '.join(['hi','my','name','is', 'Salahuddin'])

print(n_sentence)

# List Unpacking
a, b, c ,*other , d= [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(other)
print(d) 

a = None
print(a)

# DICTIONARY Unordered Key Value Pair
dict = {
    'a': 1,
    'b':[2, 3, 4, 5],
    'c':True,
    'd':{'a':1, 'b':2},
    'e':"Syed Salahuddin",
    'f':9
}
print(dict['d'])

# dictionary inside a List
my_list = [
    {
     'a':[1, 2, 3],
     'b':'hello',
     'x':True},
    {
    's':[2, 3, 4],
    'f':'Salahuddin',
    'x':False 
    }
]
print(my_list[0]['a'][2])

# In dictionary Keys can't be mutable i.e lists etc
# Keys should be unique
# Use .get() when not certain of the answer
# Keys can't be expression

user = {
    'basket':[1, 2, 3],
    'greet':'hello',
    'age':20
}

print('size' in user.keys())

print('hello' in user.items())

# Dictionary Methods
# https://www.w3schools.com/python/python_ref_dictionary.asp

# TUPLES

# Immutable Lists
# Allows accessing 
mt = (1, 2, 3, 4, 50)
print(mt)

print(user.items())

# Tuple Methods
# https://www.w3schools.com/python/python_ref_tuple.asp


my_tuple = (1, 2, 3, 4, 5)
print(my_tuple.index(4))
# Len Functions also works in tuples

# SET
# Unordered collections of unique objects
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
my_set.add(1)
print(my_set)
# If iterating over is required then convert it to list and from set and vice versa
# SET doesn't support indexing

# Set Methods
# https://www.w3schools.com/python/python_ref_set.asp
# isdisjoint to check whether they are common or not
