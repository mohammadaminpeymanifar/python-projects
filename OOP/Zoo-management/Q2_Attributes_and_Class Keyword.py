#Attributes and Class KeyWord
class animal :
    def __init__(self,name,species ,age , sound) :
        self.name = name
        self.age = age
        self.sound = sound
        self.species = species

    def make_sound(self) :
        print(self.sound)

lion = animal("leo","lion",5,"Roar")
lion.make_sound()