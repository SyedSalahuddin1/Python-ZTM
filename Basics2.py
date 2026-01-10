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

# ENUMERATE() works on list tuple 
for i, char in enumerate('Hello'):
    print(i, char)
    
for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f"index of 50 is: {char}")
        
for i, char in enumerate(list(range(0, 100, 10))):
    print(i, char)
    
# WHILE CONDITION

i = 0
while i < 50:
    print(i)
    i += 10
print("Done all iterations!")

# 2
my_list = [1, 2, 3]
for _ in my_list:
    print(_)
    
print("Break!")
i = 0
while i < len(my_list):
    print(my_list[i])
    i+=1

print("Break Again")

# while True:
#     s = input("Say Something: ")
#     print(s)
#     if s == "bye":
#         break

print("BA")

# continue
# pass 

def say_my_name():
    return "Syed Salahuddin!"

for i in range(1,10,2):
    # print(i)
    print(f"{say_my_name()} {i}")

# Arguments VS Parameters
# Default Parameters -> Given during function definition
# positional vs keyword arguments
def say_hello(name, emoji):
    print(f"Hello {name} {emoji}")

# positional arguments 
say_hello('Arman', "😀")

# Keyword arguments
say_hello(emoji="🤩", name="Khabib")


# return 
def sum1(num1, num2):
    return num1 + num2

print(sum1(2, 4))

# A function should do one thing really well.
# Should return something

def summ(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    return another_func(num1, num2)
    # return is the last code to work functionally 
    # after that it's dummy

total = summ(25, 20)
print(summ(10, 29))
print(total)

# # Methods vs Functions
# list()
# print()
# max(10, 1)
# min(100, 10)
# input()

text = "hello world"
print(text.capitalize())

# DOCSTRING
def test(a):
    '''
    Info: this function tests and prints param
    '''
    print(a)

help(test)

print(test.__doc__) 

# clean code
def is_odd_or_even(num):
    # if num % 2 == 0:
    #     return True
    # return False
    return num % 2 == 0 
    
print(is_odd_or_even(45))


# # # *args **kwargs
def super_func(*args, **kwargs):
    # print(args)
    print(kwargs)
    total = 0
    for items in kwargs.values():
        total += items 
    return sum(args) + total

print(super_func(1, 2, 3, 4, 5, num1 =5, num2=10))

# Rule: params, *args, default parameters, **kwargs

# :=
# walrus operator 
# assigns values to variables as part of larger expression

a = 'Syed Salahuddin'

if ((n := len(a)) > 10):
    print(f"too long {n} elements")
    
print("BA")
while ((n := len(a)) > 1):
    print(n)
    a = a[:-1]

# Scope -> what variables do I have access to
# if not inside a function then it is global scope

# 1 - Start with local
# 2 - Parent local?
# 3 - Global 
# 4 - Built-in Python Function
# 5 - Parameters == Local Variables
# 6 - Global variable Keyword


print("BA")

a = 1
def parent():
    a = 10
    def confusion():
        return a 
    return confusion()

print(parent())
print(a)

totall = 0

def count(totall):
    totall += 1
    return totall

print(count(count(count(totall))))

# nonlocal Keyword not a global variable but outside the scope of the function
def outer():
    x = "local"
    def inner():
        nonlocal x
    x = "nonlocal"
    print("inner:", x)
    
    inner()
    print("outer: ", x)
    
outer()
