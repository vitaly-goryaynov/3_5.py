import random
from random import randint as rd


class Dinosaur:
    def __init__(self, name, health, damage, endurance) -> None:
        self.__name = name
        self.__health = health
        self.__damage = damage
        self.__endurance = endurance
        self.__endurance_price_attack = 10

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_health(self) -> int:
        return self.__health

    def set_health(self, health: int) -> None:
        self.__health = health

    def get_damage(self) -> int:
        return self.__damage

    def set_damage(self, damage: int) -> None:
        self.__damage = damage

    def get_endurance(self) -> int:
        return self.__endurance

    def set_endurance(self, endurance: int) -> None:
        self.__endurance = endurance

    def get_endurance_price_attack(self) -> int:
        return self.__endurance_price_attack

    def set_endurance_price_attack(self, endurance_price_attack: int) -> None:
        self.__endurance_price_attack = endurance_price_attack

    def attack(self, target) -> None:
        print(f'{self.__name} атакует {target.get_view()}')

        target.take_damage(self.__damage)
        self.__endurance -= self.__endurance_price_attack

    def take_damage(self, amount: int) -> None:
        if amount > 0:
            if amount < self.__health:
                self.__health = self.__health - amount
            else:
                self.__health = 0
                self.death_dino()

    def death_dino(self) -> None:
        if self.__health == 0:
            print(f'{self.__name} погибает')

    def display_info(self) -> str:
        return f'Имя динозавра {self.__name}, здоровье динозавра {self.__health}, \nсила атаки {self.__damage}, выносливость {self.__endurance}'

    def rest(self) -> int:
        reserve = rd(1, 2)
        if reserve == 1:
            self.__endurance = self.__endurance + 10
        return self.__endurance


class Prey:
    def __init__(self, view, health) -> None:
        self.__view = view
        self.__health = health

    def is_can_flee(self) -> bool:
        is_flee = rd(1, 2)
        if is_flee == 1:
            print(f'{self.__view} удалось сбежать')
            return True

    def get_view(self) -> str:
        return self.__view

    def set_view(self, view: str):
        self.__view = view

    def get_health(self) -> int:
        return self.__health

    def set_health(self, health: int):
        self.__health = health

    def take_damage(self, amount: int):
        if amount > 0:
            if self.__health > amount:
                self.__health = self.__health - amount
            else:
                self.__health = 0

    def display_info(self) -> str:
        return f'Вид животного {self.__view}, здоровье животного {self.__health}'

    def death_prey(self) -> None:
        if self.__health == 0:
            print('Животное-добыча погибает')


class Ecosystem:
    def __init__(self) -> None:
        self.__prey = []
        self.__dinosaurs = []

    def add_dinosaur(self, dino: object) -> None:
        self.__dinosaurs.append(dino)

    def add_prey(self, prey: object) -> None:
        self.__prey.append(prey)

    def get_prey(self) -> list:
        return self.__prey

    def get_dinosaurs(self) -> list:
        return self.__dinosaurs

    def index_prey(self) -> str:
        index_prey = random.randrange(len(self.__prey))
        prey = self.__prey[index_prey]
        return prey

    def index_dinosaurs(self):
        count_dinosaurs = random.sample(self.__dinosaurs, 2)
        return count_dinosaurs

    def is_checking_entity(self) -> bool:
        if len(self.__dinosaurs) < 2:
            print('Симуляция не может быть осуществлена, динозавры отсутствуют.')
            return False
        if len(self.__prey) == 0:
            print("Симмуляция не может быть осуществлена, добыча отсутствует")
            return False
        return True

    def simulate_hunting_for_prey(self) -> None:
        if self.is_checking_entity() == True:
            prey = self.index_prey()

            count_dinosaurs = self.index_dinosaurs()
            dino_one = count_dinosaurs[0]
            dino_two = count_dinosaurs[1]
            print(f'{dino_one.get_name()} выследил {prey.get_view()} и готовится атаковать!')

            if prey.is_can_flee() != True:
                count = 0

                while prey.get_health() != 0 and dino_one.get_endurance() != 0:
                    dino_one.attack(prey)
                    count += 1
                    print(f'Атака прошла успешно! {count} круг симмуляции окончен')
            if prey.get_health() == 0:
                prey.death_prey()

            if dino_one.get_endurance() == 0:
                print('У динозавра закончилась энергия')
                if prey.get_health() != 0:
                    print('Добыча ранена, но ещё жива')

            if prey.get_health() != 0:
                print(f'{dino_two.get_name()} выследил {prey.get_view()} и готовится атаковать!')

                if prey.is_can_flee() != True:
                    count = 0
                    while prey.get_health() != 0 and dino_two.get_endurance() != 0:
                        dino_two.attack(prey)
                        count += 1
                        print(f'Атака прошла успешно! {count} круг симмуляции окончен')
                        prey.death_prey()

                        if dino_two.get_endurance() == 0:
                            print('У динозавра закончилась энергия')
                            if prey.get_health() != 0:
                                print('Добыча ранена, но ещё жива')


d1 = Dinosaur('Rexic', 100, 10, 20)
d2 = Dinosaur('Ti-Rex', 100, 20, 20)
d3 = Dinosaur('Vasiliy', 100, 20, 10)
p1 = Prey('Artiodactyl', 20)
p2 = Prey('Mamont', 60)

e1 = Ecosystem()
e1.add_dinosaur(d1)
e1.add_dinosaur(d2)
e1.add_dinosaur(d3)
e1.add_prey(p1)
e1.add_prey(p2)
e1.simulate_hunting_for_prey()
