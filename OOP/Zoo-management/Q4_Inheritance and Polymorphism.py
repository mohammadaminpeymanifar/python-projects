#Inheritance and Polymorphism
class Animal:
    def __init__(self,name,species ,age,sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound
    def make_sound(self):
        print(self.sound)

class Bird(Animal):
    def __init__(self,name,species,age,sound,wing_span):
        super().__init__(name,species,age,sound)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"Bird Sound: {self.sound}")

parrot = Bird("coco","parrot",2,"Chirp",25)
parrot.make_sound()