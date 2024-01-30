# # Задание № 6.1
# class Animal:
#     def __init__(self, name, species, age=0, weight=0, is_domestic=True):
#         self.__name = name
#         self.__species = species
#         self.__age = age
#         self.__weight = weight
#         self.__is_domestic = is_domestic
#
#     def __str__(self) -> str:
#         return f'Имя животного {self.__name}, вид животного {self.__species}, возраст {self.__age}, \nвес {self.__weight}, является домашним {self.__is_domestic}'
#
#     def get_name(self) -> str:
#         return self.__name
#
#     def set_name(self, name:str):
#         self.__name = name
#
#     def get_species(self) -> str:
#         return self.__species
#
#     def set_species(self, species:str):
#         self.__species = species
#
#     def get_age(self) -> int:
#         return self.__age
#
#     def set_age(self, age:int):
#         self.__age = age
#
#     def get_weight(self) -> float:
#         return self.__weight
#
#     def set_weight(self, weight:float):
#         self.__weight = weight
#
#     def get_is_domestic(self) -> bool:
#         return self.__is_domestic
#
#     def set_is_domestic(self, is_domestic: bool):
#         self.__is_domestic = is_domestic
#
#     def make_sound(self, sound:str) -> str:
#         return f'Животное издало звук {sound}'
#
#
#     def feed(self, food:float) -> str:
#         if food > 0:
#             self.__weight = self.__weight + food
#         else:
#             return f'Введите корректное значение'
#
#
# a1 = Animal('Бегемот', "кот", 1, 1)
# print(a1)
# a1.set_name('lex')
# a1.feed(0.1)
# print(a1)

# 6.2

# class Pizza:
#     def __init__(self, name, size=18, price=50):
#         self.__name = name
#         self.__ingredients = []
#         self.__size = size
#         self.__price = price
#
#
#     def __str__(self):
#         return f'Название пиццы {self.__name}, список ингридиентов {self.__ingredients}, \nразмер пиццы {self.__size}, цена пиццы {self.__price}'
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, name):
#         self.__name = name
#
#     def get_size(self):
#         return self.__size
#
#     def get_price(self):
#         return self.__price
#
#     def add_ingredients(self, ingredient):
#         self.__ingredients.append(ingredient)
#
#     def get_ingredients(self):
#         return self.__ingredients
#
#     def calculate_price(self):
#         count = len(self.__ingredients)
#         if count > 0:
#             self.__price = self.__price * count
#
#     def order_size(self, size):
#         if size == 18:
#             self.__size = 18
#             self.__price = self.__price + 200
#         elif size == 25:
#             self.__size = 25
#             self.__price= self.__price + 300
#         elif size == 30:
#             self.__size = 30
#             self.__price = self.__price + 400
#         elif size == 35:
#             self.__size = 35
#             self.__price = self.__price + 500
#         else:
#             print('Недопустимый размер пиццы')
#
#
# p1 = Pizza('peperony', )
# p1.order_size(25)
# p1.add_ingredients('salyami')
# p1.add_ingredients('ogurci')
# p1.calculate_price()
# print(p1)

# 6.3

class Cafe:
    def __init__(self, name) -> None:
        self.__name = name
        self.__menu = []

    def __str__(self) -> str:
        return f'Кафе {self.__name}. Список блюд: {self.__menu}'

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    def order_products(self):
        pass

    def display_menu(self) -> list:
        return self.__menu

    def add_dish(self, dish: str) -> None:
        self.__menu.append(dish)


class Suppler:
    def __init__(self, name) -> None:
        self.__name = name
        self.__product_list = []

    def __str__(self) -> str:
        return f'Поставщик {self.__name}, \nсписок поставляемых продуктов {self.__product_list}'

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def display_products(self) -> list:
        return self.__product_list

    def add_product(self, product: str):
        self.__product_list.append(product)

    def dell_product(self, product: str):
        self.__product_list.remove(product)