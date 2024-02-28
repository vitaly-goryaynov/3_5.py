from __future__ import annotations


class Hero:
    def __init__(self, name: str, health: int):
        self.__name = name
        self.__health = health
        self.__inventory = []

    def pick_up(self, item: Item):
        self.__inventory.append(item)

    def use_item(self, item_name: str):
        for i in self.__inventory:
            if item_name == i:
                print(f"Использование предмета {i}")

    def fight(self, monster: Monster):
        print(f"Герой атакует {monster}")

    def take_damage(self, amount: int):
        if amount > 0 and self.__health > 0:
            if self.__health > amount:
                self.__health -= amount

            else:
                self.__health = 0
                print('Герой погибает')


class Item:
    def __init__(self, name: str, type_armament: str):
        self.__name = name
        self.__type_armament = type_armament


class Monster:
    def __init__(self, name: str, power: int):
        self.__name = name
        self.__power = power

    def attack(self, hero: Hero):
        print(f'{self.__name} атакукет {hero}')
        hero.take_damage(self.__power)

class Dungeon:
    def __init__(self):
        self.__monsters = []
        self.__things = []

    def add_monster(self, monster: Monster):
        self.__monsters.append(monster)

    def add_thing(self, thing: Item):
        self.__things.append(thing)

    def __calculate_finding_thing(self):
        from random import randint as rd
        len_list = len(self.__things)
        n = rd(1, len_list)
        thing = self.__things[n-1]
        return thing

    def __calculate_meeting_monster(self):
        from random import randint as rd
        len_list = len(self.__monsters)
        n = rd(1, len_list)
        monster = self.__monsters[n-1]
        return monster

    def explore(self, hero: Hero):
        if len(self.__monsters) < 2:
            print('Для симмуляции исследования подземелья добавьте монстов')
            print(len(self.__monsters))
            return
        if len(self.__things) < 2:
            print('Для симмуляции исследования подземелья добавьте предметы героя')
            return

        # from random import randint as rd
        # calculate_scenario = rd(1, 2)
        # if calculate_scenario == 1:
        thing = self.__calculate_finding_thing()
        hero.pick_up(thing)
        # hero.use_item(thing)









h1 = Hero('Vasiliy', 100)
d = Dungeon()
m1 = Monster('Zubastik', 10)
d.add_monster(m1)
m2 = Monster('Gadzila', 20)
d.add_monster(m2)
m3 = Monster('Slizn9k', 10)
d.add_monster(m3)
i1 = Item('armor Zeus', 'armor')
d.add_thing(i1)
i2 = Item('stel sword', 'weapon')
d.add_thing(i2)
i3 = Item('helmet', 'armor')
d.add_thing(i3)
i4= Item('bow and arrow', 'weapon')
d.add_thing(i4)
h1.use_item('armor Zeus')


d.explore(h1)