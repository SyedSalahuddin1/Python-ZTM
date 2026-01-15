class User:
    def sign_in(self):
        print("Logged In")

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power 
        
    def attack(self):
        print(f"Attacking with power of {self.power}")

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows 
        
    def attack(self):
        print(f"Attacking with arrows: arrows left - {self.num_arrows}")

    def run(self):
        print('ran really fast!')
        
    def check_arrows(self):
        print(f"{self.num_arrows} remaining")
wizard1 = Wizard("Melrin", 50)
archer1 = Archer("Robin", 100)
print(wizard1.sign_in())

wizard1.attack()
archer1.attack()
    
print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))
print(isinstance(wizard1, object))

class HybridCar(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)
        # super().__init__(name, power)

hb1 = HybridCar("borgi", 20, 500)
print(hb1.check_arrows())
print(hb1.run())
print(hb1.attack())
    
