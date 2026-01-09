# Conditional Logic
# Indentation in Python
# Truthy and Falsy = printing True or False using bool
# Example
password = "1234"
username = "jonny"

if username and password:
    print("You are old enough to drive, and you have licence!")
else:
    print("you are not of age!")

print('OKOKO')

# Ternary Operator = Conditionol Expression

# condition_if_true if condition else condition_if_else

is_friend = True
can_message = "message allowed" if is_friend else "message not allowed"
print(can_message)

# Short Circuiting
# Using and or 
# Printing True or False for conditions


is_friend = True 
is_user = True 

print(is_friend and is_user)

# Logical Operator
# > < == != <

# is VS ==
# == checks for equality
# is checks if the location of memory where e value is stored is same
# is gives True for numbers

# Has different o/p for == and is
print(True is 1)
print('1' is 1)
print([] is 1)
print(10 is 10)
print([1, 2, 3] is [1, 2, 3])

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)


# LOOPS

for item in "Syed Salahuddin":
    print(item)

# Nested Loops 
# $ loop inside a loop

# iterable -- list, dictionary, tuple, set, string
# iterated -> one by one check each item in the collection

# for key, value in user.items():
#   print(key, value)