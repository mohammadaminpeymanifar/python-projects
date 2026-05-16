#OOP Introduction:
class animal:

    def __init__(self, name , species , age , sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

lion = animal("Leo" , "Lion" , 5 , "Roar")

print(lion.name)
print(lion.species)
print(lion.age)
print(lion.sound)