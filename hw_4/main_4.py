## Задание №4
# #4.1
#
# class Recipe:
#     def __init__(self, name, instruction, ingredients=None):
#         self.__name = name
#         self.__instruction = instruction
#         self.__ingredients = []

#     def __str__(self):
#         return f"Название рецепта {self.__name}, состав: {self.__ingredients}, инструкция приготовления: {self.__instruction}"
#
#     def set_name(self, name):
#         if len(name) > 0:
#             self.__name = name
#         else:
#             check_recipe()
#
#     def get_name(self):
#         return self.__name
#
#     def set_instruction(self,instruction):
#         if len(instruction) > 0:
#             self.__instruction = instruction
#         else:
#             check_recipe()
#
#     def get_instruction(self):
#         return self.__instruction
#
#     def get_ingredient(self):
#         return self.__ingredients
#
#     def set_ingredient(self, ingredient):
#         if len(ingredient) > 0:
#             self.__ingredients.append(ingredient)
#         else:
#             check_recipe()
#     def del_ingredient(self, ingredient):
#         self.__ingredients.remove(ingredient)
#
# def check_recipe():
#     print('Заполните данные рецепта!')
#
#
# r1 = Recipe('суп', 'варить' )
# r1.set_name('')
# print(r1)
# r1.set_name('щи')
# print(r1)
# r1.set_ingredient('')
# print(r1)
# r1.set_ingredient('мясо')
# print(r1)
#
##4.2
#
# class SpaceMission:
#     def __init__(self,mission, task, date, name=None):
#         self.__mission = mission
#         self.__task = task
#         self.__name = []
#         self.__date = date
#
#     def __str__(self):
#         return f"Название миссии: {self.__mission}, список имён членов экипажа {self.__name}, дата запуска {self.__date} "
#
#     def add_name(self, name:str) -> [str]:
#         if len(name) > 0:
#             self.__name.append(name)
#         else:
#             print('Проверьте правильность заполнения данных')
#
#     def get_name(self) -> [str]:
#         return self.__name
#
#     def set_date(self, date:str):
#         if len(date) > 0:
#             if date == str:
#                 self.__date = date
#         else:
#             print('Введите данные космонавта')
#
#     def get_date(self) -> str:
#         return self.__date
#
#
# s1 = SpaceMission('Космический полёт', 'Марс', "17.01.2024")
# print(s1)
# s1.add_name('Vova')
# s1.add_name('Vlad')
# print(s1.get_name())
# print(s1)
#
##4.3
#
# class Animal:
#     def __init__(self, view, name, age, place):
#         self.__view = view
#         self.__name = name
#         self.__age = age
#         self.__place = place
#
#     def __str__(self):
#         return f'Вид животного {self.__view}, имя животного {self.__name}, возраст {self.__age}'
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, age):
#         if age > 0 :
#             self.__age = age
#         else:
#             print('Введите корректное значение')
#     def get_place(self):
#         return self.__place
#
#     def set_place(self, place):
#         if len(place) > 0:
#             self.__place = place
#         else:
#             print('Проверьте правильность заполнения данных')
#
# a1 = Animal('кот', "Василий", "5", 'Vlz')
# a1.set_age(6)
# print(a1)
#
##4.4
#
#
class Hogwarts:
    pass

class StudentHogwarts:
    pass

class Spell:
    pass