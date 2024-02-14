class Animal:
    def __init__(self, name: str, age: int, vertebrates: bool):
        self.name = name
        self.age = age
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
        return f'Имя {self.name}, возраст {self.age}, вскармливаелся молоком {self.feed_milk}, \nподтип позвоночные {self.vertebrates}, умение точить когти {self.sharpen_claws}'


class Dog(Mammal):
    def __init__(self, name: str, age: int, vertebrates=True, feed_milk=True, drooling=True):
        Mammal.__init__(self, name, age, vertebrates, feed_milk)
        self.drooling = drooling

    def __str__(self):
        return f'Имя {self.name}, возраст {self.age}, вскармливаелся молоком {self.feed_milk}, \nподтип позвоночные {self.vertebrates}, пускает слюни {self.drooling}'


class Bird(Animal):
    def __init__(self, name: str, age: int, vertebrates: bool, have_feathers: bool):
        Animal.__init__(self, name, age, vertebrates)
        self.have_feathers = have_feathers


class Sparrow(Bird):
    def __init__(self, name: str, age: int, vertebrates=True, have_feathers=True, lives_on_street=True):
        Bird.__init__(self, name, age, vertebrates, have_feathers)
        self.lives_on_street = lives_on_street

    def __str__(self):
        return f'Вид {self.name}, возраст {self.age}, подтип позвоночные {self.vertebrates}, \nесть перья {self.have_feathers}, живёт на улице {self.lives_on_street}'


class Parrot(Bird):
    def __init__(self, name: str, age: int, vertebrates=True, have_feathers=True, can_say=True):
        Bird.__init__(self, name, age, vertebrates, have_feathers)
        self.can_say = can_say

    def __str__(self):
        return f'Вид {self.name}, возраст {self.age}, подтип позвоночные {self.vertebrates}, \nесть перья {self.have_feathers}, может говорить {self.can_say}'



class Amphibian(Animal):
    def __init__(self, name: str, age: int, vertebrates: bool, born_larva:bool):
        Animal.__init__(self, name, age, vertebrates)
        self.born_larva = born_larva


class Frog(Amphibian):
    def __init__(self,  name: str, age: int, vertebrates=True, born_larva=True, jump=True):
        Amphibian.__init__(self, name, age, vertebrates, born_larva)
        self.jump = jump

    def __str__(self):
        return f'Вид {self.name}, возраст {self.age}, подтип позвоночные {self.vertebrates}, \nрождается личинкой {self.born_larva}, прыгает {self.jump}'

class Salamander(Amphibian):
    def __init__(self, name: str, age: int, vertebrates=True, born_larva=True, tail=True):
        Amphibian.__init__(self, name, age, vertebrates, born_larva)
        self.tail = tail

    def __str__(self):
        return f'Вид {self.name}, возраст {self.age}, подтип позвоночные {self.vertebrates}, \nрождается личинкой {self.born_larva}, есть хвост {self.tail}'


class Reptile(Animal):
    def __init__(self, name: str, age: int, vertebrates: bool, lay_eggs_in_soil:bool):
        Animal.__init__(self, name, age, vertebrates)
        self.lay_eggs_in_soil = lay_eggs_in_soil


class Turtle(Reptile):
    def __init__(self, name: str, age: int, vertebrates=True, lay_eggs_in_soil=True, shell=True):
        Reptile.__init__(self, name, age, vertebrates, lay_eggs_in_soil)
        self.shell = shell

    def __str__(self):
        return f'Вид {self.name}, возраст {self.age}, подтип позвоночные {self.vertebrates}, \nоткладывают яйца в почву {self.lay_eggs_in_soil}, есть панцирь {self.shell}'


class Boa(Reptile):
    def __init__(self, name: str, age: int, vertebrates=True, lay_eggs_in_soil=True, long_tail=True):
        Reptile.__init__(self, name, age, vertebrates, lay_eggs_in_soil)
        self.long_tail = long_tail

    def __str__(self):
        return f'Вид {self.name}, возраст {self.age}, подтип позвоночные {self.vertebrates}, \nоткладывают яйца в почву {self.lay_eggs_in_soil}, длинный хвост {self.long_tail}'


class Fish(Animal):
    def __init__(self, name: str, age: int, vertebrates: bool, live_in_water:bool):
        Animal.__init__(self, name, age, vertebrates)
        self.live_in_water = live_in_water


class Carp(Fish):
    def __init__(self, name: str, age: int, vertebrates=True, live_in_water=True, hunt_in_river=True):
        Fish.__init__(self, name, age, vertebrates, live_in_water)
        self.hunt_in_river = hunt_in_river

    def __str__(self):
        return f'Вид {self.name}, возраст {self.age}, подтип позвоночные {self.vertebrates}, \nживут вводе {self.live_in_water}, охотятся в реке {self.hunt_in_river}'


class Shark(Fish):
    def __init__(self, name: str, age: int, vertebrates=True, live_in_water=True, hunt_in_sea=True):
        Fish.__init__(self, name, age, vertebrates, live_in_water)
        self.hunt_in_sea = hunt_in_sea

    def __str__(self):
        return f'Вид {self.name}, возраст {self.age}, подтип позвоночные {self.vertebrates}, \nживут вводе {self.live_in_water}, охотятся в море {self.hunt_in_sea}'


c1 = Cat('Vasily', 10)
d2 = Dog('Rex', 2)
print(c1)
print(d2)
