# # Задание № 3.6.1

class Animal:
    def __init__(self, name:str, species:str, age=0, weight=0, is_domestic=True):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__weight = weight
        self.__is_domestic = is_domestic

    def __str__(self) -> str:
        return f'Имя животного {self.__name}, вид животного {self.__species}, возраст {self.__age}, \nвес {self.__weight}, является домашним {self.__is_domestic}'

    def get_is_domestic(self) -> bool:
        return self.__is_domestic

    def set_is_domestic(self, is_domestic: bool):
        self.__is_domestic = is_domestic

    def make_sound(self, sound:str) -> str:
        return f'Животное издало звук {sound}'

    def feed(self, food:float) -> str:
        if food > 0:
            self.__weight = self.__weight + food
        else:
            return f'Введите корректное значение'

#
# a1 = Animal('Бегемот', "кот", 1, 1)

# print(a1)

# a1.set_name('lex')
# a1.feed(0.1)

# print(a1)

# 6.2

class Pizza:
    def __init__(self, name: str, size=18, price=50):
        self.__name = name
        self.__ingredients = []
        self.__size = size
        self.__price = price

    def __str__(self) -> str:
        return f'Название пиццы {self.__name}, список ингридиентов {self.__ingredients}, \nразмер пиццы {self.__size}, цена пиццы {self.__price}'

    def get_name(self) -> str:
        return self.__name

    def add_ingredients(self, ingredient: str):
        self.__ingredients.append(ingredient)

    def get_ingredients(self) -> list:
        return self.__ingredients

    def calculate_price(self) -> None:
        count = len(self.__ingredients)
        if count > 0:
            self.__price = self.__price * count

    def order_size(self, size):
        if size == 18:
            self.__size = 18
            self.__price = self.__price + 200
        elif size == 25:
            self.__size = 25
            self.__price= self.__price + 300
        elif size == 30:
            self.__size = 30
            self.__price = self.__price + 400
        elif size == 35:
            self.__size = 35
            self.__price = self.__price + 500
        else:
            print('Недопустимый размер пиццы')

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
        self.__menu = ['лаваш', "мясо", "помидор", "капуста"]

    def __str__(self) -> str:
        return f'Кафе {self.__name}. Список необходимых продуктов: {self.__menu}'

    def order_products(self, supplier):
        for i in supplier.display_products():
            if i in self.__menu:
                print(f"Ингредиент {i} поставляет {supplier.get_name()}")

    def display_menu(self) -> list:
        return self.__menu

    def add_product_in_menu(self, product: str) -> None:
        self.__menu.append(product)

class Suppler:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__product_list = []

    def __str__(self) -> str:
        return f'Поставщик {self.__name}, \nсписок поставляемых продуктов {self.__product_list}'

    def get_name(self) -> str:
        return self.__name

    def display_products(self) -> list:
        return self.__product_list

    def add_product(self, product: str):
        self.__product_list.append(product)

    def dell_product(self, product: str):
        self.__product_list.remove(product)

#
# c1 = Cafe('Шаурма Влз')
#
# s1 = Suppler('Мясодел.рф')
# s2 = Suppler('Хлебопёк')
# s3 = Suppler('Ботаник')
#
# s1.add_product('мясо')
# s2.add_product('лаваш')
# s3.add_product('помидор')
# s3.add_product('капуста')
#
# c1.order_products(s1)
# c1.order_products(s3)

# 6.4

class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.__title = title
        self.__author = author
        self.__year = year

    def __str__(self) -> str:
        return f'Название книги: {self.__title}, автор {self.__author}, год издания: {self.__year};'


class Library:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__books = []

    def add_book(self, book: object) -> None:
        if book not in self.__books:
            self.__books.append(book)
            print(f'{book} - книга добавлена в список книг')
        else:
            print(f'{book} - книга уже есть в библиотеке')

    def remove_book(self, book: object) -> None:
        if book not in self.__books:
            print(f'{book} книга отсутствует в библиотеке')
        else:
            self.__books.remove(book)
            print(f'{book} удалена из списка книг')

    def display_books(self) -> list:
        return self.__books


b1 = Book('Война миров', 'Дарт Вейдер', 2025)
b2 = Book('Кошки правят миром', "Василий Рыжий", 2030)

l1 = Library("Городская библиотека")

l1.add_book(b1)
l1.add_book(b1)
l1.add_book(b2)
l1.remove_book(b1)

print(*l1.display_books())


# 6.5


class Component:
    def __init__(self, name: str, type: str) -> None:
        self.__name = name
        self.__type = type

    def __str__(self) -> str:
        return f"Название компонента - {self.__name}, тип компонента - {self.__type}"


class Computer:
    def __init__(self, model: str) -> None:
        self.__model = model
        self.__components = []

    def create_component(self, name: str, type: str) -> object:
        component = Component(name, type)
        return component

    def add_component(self, component: object) -> None:
        if component not in self.__components:
            self.__components.append(component)
            print(f'{component}, добавлен в список компонентов компьютера')
        else:
            print(f'Такой компонет уже есть в списке компонентов компьютера')

    def remove_component(self, component: object) -> None:
        if component not in self.__components:
            print(f"Компонента с таким именем не существует")
        else:
            self.__components.remove(component)
            print(f'{component}, удалён из списка компонентов компьютера')


    def display_components(self) -> None:
        for i in self.__components:
            print(i, end=' ')

    def __del__(self):
        for component in self.__components:
            del component


# pc = Computer('Пентагон 666')
#
# cc1 = pc.create_component('видеокарта', "микросхема")
# cc2 = pc.create_component("клавиатура", "устройство ввода")
#
# com1 = pc.add_component(cc1)
# com2 = pc.add_component(cc2)
# com3 = pc.remove_component(cc2)
#
# pc.display_components()
# del pc




