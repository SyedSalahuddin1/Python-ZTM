# # Data Types

# 1.int
# 2.float
# 3.str  immutable 
# 4.bool
# 5.list
# 6.set
# 7.dict
# 8.tuple
# complex
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