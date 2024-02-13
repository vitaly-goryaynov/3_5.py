class WorldAnimal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

class Animal(WorldAnimal):
    def __init__(self, name: str, age: int, vertebrates: bool):
        WorldAnimal.__init__(self, name, age)
        self.vertebrates = vertebrates

class Mammal(Animal):
    def __init__(self, name: str, age: int, vertebrates: bool, feed_milk: bool):
        Animal.__init__(self, name, age, vertebrates)
        self.feed_milk = feed_milk

class Cat(Mammal):
    def __init__(self, name: str, age: int, vertebrates=True, feed_milk=True, sharpen_claws=True):
        Mammal.__init__(self, name, age, vertebrates, feed_milk)
        self.sharpen_claws = sharpen_claws

    def __str__(self):
        return f'{self.name}, {self.age}, {self.feed_milk}, {self.vertebrates}, {self.sharpen_claws}'

c1 = Cat('Vasily', 10)
print(c1)