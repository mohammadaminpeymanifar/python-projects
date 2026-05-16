#Magic/Dunder Methods
class animal:
    def __init__(self,name,species,age):
        self.name = name
        self.species = species
        self.age = age

    def __str__(self):
        return f"{self.name} is a {self.species}, Age: {self.age}"

lion = animal("len",'Lion',5)
print(lion)