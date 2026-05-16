#Class Object Attributes and Methods
class animal:

    Zoo_name= "Wild Zoo"

    def __init__(self, name , species , age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

    def info(self):
        print(f"Zoo nema:{animal.Zoo_name}")
        print(f"name:{self.name}")
        print(f"Species:{self.species}")
        print(f"Age:{self.age}")
        print(f"Sound:{self.sound}")

lion = animal("Leo","Lion",5,"Roar")
lion.info()