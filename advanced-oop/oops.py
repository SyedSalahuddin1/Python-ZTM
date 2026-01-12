# OOP allows us to write code i.e repeatable, well organized and also memory effecient
# Grouping data with methods and attributes
class BigObject:
    pass

obj1 = BigObject()

print(type(obj1))
# class name CamelCase
# Class Instanctiates Instances

class PlayerCharacter:
    #Class Object Attribute
    membership = True
    
    # Constructor Method or Init Method
    # Constructor Function
    def __init__(self, name, age):
        self.name = name #attributes / properties
        self.age = age 
    
    # methods
    def run(self):
        # if a function doesn't return anything it return none
        print('run')
        return 'done'
    
    @classmethod 
    def adding_things(cls, num1, num2):
        return num1 + num2
    
    @classmethod
    def multiplied_things(cls, num1, num2):
        return cls("Makrs", num1*num2)
    
player1 = PlayerCharacter("Striker", 22)
player2 = PlayerCharacter("Forward", 30)

print(player1.name, player1.age)
print(player2.name, player2.age)
player1.membership = False

print(player2.run())
# help(player1)
print(player1.membership)
print(player1.adding_things(22, 32))

print(PlayerCharacter.adding_things(41,122))

player3 = PlayerCharacter.multiplied_things(12, 6)

print(player3.age)