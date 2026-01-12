class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
        
    def run(self):
        print('run')
        
    def speak(self):
        print(f"My name is {self.name} and I am {self.age} years old.")
    
player1 = PlayerCharacter('Salahuddin', 24)
player1.speak()

player2 = PlayerCharacter('Lewondwaski', 32)
player2.name = "Fool"
player2.speak = lambda : print("BOOOOO!!")

print(player2.speak())
print(player2.name)
