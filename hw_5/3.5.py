import random
from random import randint as rd


class Dinosaur:
    def __init__(self, name, health, damage, endurance):
        self.__name = name
        self.__health = health
        self.__damage = damage
        self.__endurance = endurance
        self.__endurance_price_attack = 10

    def attack(self, target) -> int or str:
        print(f'Атака на {target.get_view()}')
        target.take_damage(self.__damage)
        self.__endurance -= self.__endurance_price_attack

    def get_endurance(self):
        return self.__endurance

    def take_damage(self, amount: int) -> int:
        if amount > 0:
            if amount < self.__health:
                self.__health = self.__health - amount
            else:
                self.__health = 0
                # TODO: Добавить метод смерти

    def death_dino(self):
        if self.__health == 0:
            return "Динозавр погиб.."

    def display_info(self) -> str:
        return f'Имя динозавра {self.__name}, здоровье динозавра {self.__health}, \nсила атаки {self.__damage}, выносливость {self.__endurance}'

    def rest(self) -> int:
        pass


class Prey:
    def __init__(self, view, health):
        self.__view = view
        self.__health = health

    def can_flee(self) -> bool:
        is_flee = rd(1, 2)
        if is_flee == 1:
            return True
        else:
            return False


    def get_view(self):
        return self.__view

    def get_health(self):
        return self.__health

    def take_damage(self, amount: int) -> int:
        if amount > 0:
            if self.__health > amount:
                self.__health = self.__health - amount
            else:
                self.death_prey()

    def display_info(self) -> str:
        return f'Вид животного {self.__view}, здоровье животного {self.__view}'


    def death_prey(self):
        if self.__health == 0:
            return 'Животное-добыча погибает'

class Ecosystem:
    def __init__(self):
        self.__prey = []
        self.__dinosaurs = []

    def add_dinosaur(self, dino: object) -> None:
        self.__dinosaurs.append(dino)

    def add_prey(self, prey: object) -> None:
        self.__prey.append(prey)

    def simulate_hunt(self):
        if len(self.__dinosaurs) < 2:
            return 'Симуляция не может быть осуществлена, динозавры отсутствуют'
        if len(self.__prey) == 0:
            return "Симмуляция не может быть осуществлена, добыча отсутствует"

        count_prey = len(self.__prey)
        prey = self.__prey[rd(1, count_prey) - 1]

        number_dinoes = random.sample(self.__dinosaurs, 2)
        dino_one = self.__dinosaurs[0]
        dino_two = self.__dinosaurs[1]

        while prey.get_health() != 0 and (dino_one.get_endurance() !=0  or dino_two.get_endurance() != 0):
            dino_one.attack(prey)
            dino_two.attack(prey)
            print('Первый круг симмуляции окончен')



d1 = Dinosaur('Rexic', 100, 30, 100)
d2 = Dinosaur('Ti-Rex', 100, 50, 100)
d3 = Dinosaur('Vasiliy', 100, 10, 100)
p1 = Prey('Artiodactyl', 50)
p2 = Prey('Proboscidea', 150)

e1 = Ecosystem()
e1.add_dinosaur(d1)
e1.add_dinosaur(d2)
e1.add_dinosaur(d3)
e1.add_prey(p1)
e1.add_prey(p2)

e1.simulate_hunt()