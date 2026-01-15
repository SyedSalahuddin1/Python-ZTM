class User:
    def __init__(self, email):
        self.email = email
        
    def sign_in(self):
        print("Logged In")
    
    def attack(self):
        print("Do Nothing")

class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email) 
        # User.__init__(self, email) 
        self.name = name
        self.power = power 
        
    def attack(self):
        User.attack(self)
        print(f"Attacking with power of {self.power}")

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows 
        
    
    def attack(self):
        
        print(f"Attacking with arrows: arrows left - {self.num_arrows}")


wizard1 = Wizard("Melrin", 50, "acd@gmail.com")
archer1 = Archer("Robin", 100)
print(wizard1.sign_in())

print(wizard1.attack())
# archer1.attack()
    
def player_attack(char):
    char.attack()
    
player_attack(wizard1)
player_attack(archer1)

print("Dir Function")

print(dir(wizard1))

