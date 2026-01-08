# # Data Types

# 1.int
# 2.float
# 3.str 
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

