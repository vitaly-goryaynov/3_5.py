from random import randint as rd
class Dinosaur:
    def __init__(self, name, health, damage, endurance):
        self.__name = name
        self.__health = health
        self.__damage = damage
        self.__endurance = endurance

    def get_attack(self) -> int:
        return self.__damage

    def set_attack(self):
        pass



    def take_damage(self, amount: int) -> int:
        if amount > 0:
            self.__health = self.__health - amount

    def display_info(self) -> str:
        return f'Имя динозавра {self.__name}, здоровье динозавра {self.__health}, \nсила атаки {self.__damage}, выносливость {self.__endurance}'

    def rest(self) -> int:
        self.__endurance = self.__endurance + (self.__endurance * 20 / 100)


class Prey:
    def __init__(self, view, health):
        self.__view = view
        self.__health = health

    def flee(self) -> bool:
        a = rd(1,2)
        if a == 1:
            return True
        else:
            return False

    def take_damage(self, amount:int) -> int:
        self.__health = self.__health - amount
        return self.__health

    def display_info(self) -> str:
        return f'Вид животного {self.__view}, здоровье животного {self.__view}'


class Ecosystem:
    def __init__(self, Dinosaur):
        self.__dinosaur = Dinosaur()
        self.__prey = Prey()
        self.__dinosaurs = []

    # def add_dinosaur(self, Dinosaur):
    #     self.__dinosaurs.append(Dinosaur)
    #
    #
    # def add_prey(self, prey) -> list:
    #     self.__prey.append(prey)

    def simulate_hunt(self, entity):
        count = 0
        for i in entity:
            count += 1
        n = rd(1, count)
        entity = entity[n]
        return entity


# d1 = Dinosaur('Rexic', 100, 30, 100)
# d2 = Dinosaur('Ti-Rex', 100, 50, 100)
# d3 = Dinosaur('Vasiliy', 100, 10, 100)
p1 =Prey('Artiodactyl', 50)
p2 = Prey('Proboscidea',  150)
e = Ecosystem('dsf', 'afgs', 'gdhd', )