class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name 
        self._age = age 
        
    def run(self):
        print('run')
        
    def speak(self):
        print(f"My name is {self._name} and I am {self._age} years old.")
    
player1 = PlayerCharacter('Salahuddin', 24)
player1.speak()

player2 = PlayerCharacter('Lewondwaski', 32)
player2.name = "Fool"
player2.speak = lambda : print("BOOOOO!!")

print(player2.speak())
print(player2.name)

# Dunder Methods -> Already have a meaning and can't be used/renamed 
