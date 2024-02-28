# 3.5
class Dinosaur:
    def __init__(self, name:str, health:int, damage:int, endurance:int, endurance_price_attack:int):
        self.__name = name
        self.__health = health
        self.__damage = damage
        self.__endurance = endurance
        self.__endurance_price_attack = endurance_price_attack
        self.__is_reserve_endurance = True

    def get_name(self) -> str:
        return self.__name

    def get_health(self) -> int:
        return self.__health

    def get_endurance(self) -> int:
        return self.__endurance

    def attack(self, target) -> None:
        print(f'{self.__name} атакует {target.get_name()}')

        target.take_damage(self.__damage)
        self.__endurance -= self.__endurance_price_attack
        print(f'Успешная атака, выносливость  {self.__endurance} ')

        if self.__endurance == 0 and self.__is_reserve_endurance:
            self.__rest()
        else:
            return

    def take_damage(self, amount: int) -> None:
        if amount > 0 and self.__health > 0:
            if amount < self.__health:
                self.__health -= amount
            else:
                self.__health = 0
                self.__death_dino()
        else:
            self.__death_dino()

    def __death_dino(self) -> None:
        if self.__health == 0:
            print(f'{self.__name} погибает')

    def display_info(self) -> None:
        print(f'Динозавр {self.__name}, здоровье {self.get_health()}, сила атаки {self.__damage}, показатель выносливости {self.__endurance}')

    def __rest(self) -> None:
        from random import randint as rd
        from random import randrange as ran
        calculate_chance_endurance = rd(1, 2)
        calculate_reserve_endurance = ran (10,  30, 10)

        if calculate_chance_endurance == 1:
            self.__endurance = self.__endurance + calculate_reserve_endurance
            print(f'Получена резервная выносливость {calculate_reserve_endurance}')
        self.__is_reserve_endurance = False


class Prey:
    def __init__(self, name: str, health: int):
        self.__name = name
        self.__health = health

    def get_name(self) -> str:
        return self.__name

    def get_health(self) -> int:
        return self.__health

    def can_flee(self) -> bool:
        from random import randint as rd
        calculate_chance_flee = rd(1, 2)
        if calculate_chance_flee == 1:
            print(f'{self.__name} удалось сбежать')
            return True
        return False

    def take_damage(self, amount: int) -> None:
        if amount > 0 and self.__health > 0:
            if self.__health > amount:
                self.__health = self.__health - amount

            else:
                self.__health = 0
                self.death_prey()

    def display_info(self) -> None:
        print(f'Добыча {self.__name}, здоровье {self.__health}')

    def death_prey(self) -> None:
        if self.__health == 0:
            print('Животное-добыча погибает')

class Ecosystem:
    def __init__(self):
        self.__prey = []
        self.__dinosaurs = []

    def add_dinosaur(self, dino: object) -> None:
        self.__dinosaurs.append(dino)

    def add_prey(self, prey: object) -> None:
        self.__prey.append(prey)

    def __calculate_index_prey(self) -> str:
        import  random
        calculate_index_prey = random.randrange(len(self.__prey))
        prey = self.__prey[calculate_index_prey]
        return prey

    def __calculate_index_dinosaurs(self) -> list:
        import random
        count_dinosaurs = random.sample(self.__dinosaurs, 2)
        return count_dinosaurs

    def __is_checking_entity(self) -> bool:
        if len(self.__dinosaurs) < 2:
            print('Симуляция не может быть осуществлена, динозавры отсутствуют')
            return False
        if len(self.__prey) == 0:
            print("Симмуляция не может быть осуществлена, добыча отсутствует")
            return False
        return True

    def __print_end(self):

        print('Симмуляция закончена')

    def simulate_hunting_for_prey(self) -> None:
        from random import randint as rd
        if not self.__is_checking_entity(): return

        prey = self.__calculate_index_prey()

        count_dinosaurs = self.__calculate_index_dinosaurs()

        calculate_dino_attack = rd(0, 1)
        if calculate_dino_attack == 0:
            dino_one = count_dinosaurs[0]
            dino_two = count_dinosaurs[1]
        else:
            dino_one = count_dinosaurs[1]
            dino_two = count_dinosaurs[0]
        if prey.can_flee():
            dino_one.display_info()
            prey.display_info()

        while prey.get_health() != 0:
            dino_one.display_info()
            prey.display_info()

            if dino_one.get_endurance() != 0:
                dino_one.attack(prey)
            elif dino_two.get_endurance() != 0:
                dino_two.display_info()
                prey.display_info()
                dino_two.attack(prey)
            else:
                print('Добыча убежала')
                self.__print_end()
                return
        self.__print_end()


d1 = Dinosaur('Rexic', 100, 10, 40, 10)
d2 = Dinosaur('Ti-Rex', 100, 10, 40, 10)
d3 = Dinosaur('Vasiliy', 100, 10, 30, 10)
p1 = Prey('Artiodactyl', 60)
p2 = Prey('Mamont', 100)

e1 = Ecosystem()

e1.add_dinosaur(d1)
e1.add_dinosaur(d2)
e1.add_dinosaur(d3)

e1.add_prey(p1)
e1.add_prey(p2)

e1.simulate_hunting_for_prey()
