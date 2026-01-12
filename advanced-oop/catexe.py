class Cat:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
    
    @staticmethod
    def oldest1(*args):
        return max(args)
        
cat1 = Cat("Britty", 3)
cat2 = Cat("Tippy", 4)
cat3 = Cat("Forry", 6)

def oldest(*age):
    return max(age)

oldest_cat = oldest(cat1.age, cat2.age, cat3.age)

eldest_cat = Cat.oldest1(cat1.age, cat2.age, cat3.age)

print(eldest_cat)

print(f"The oldest cat is {oldest_cat} years old.")
        