# # Задание №1
# # 1.1
#
# class Student:
#     def __init__(self, first_name, last_name, birth_year, specialty, list_estimates=None):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.birth_year = birth_year
#         self.specialty = specialty
#         self.list_estimates = []
#
#     def __str__(self):
#         return f'Имя студента {self.first_name}, фамилия {self.last_name}, год рождения {self.birth_year},\nспециальность {self.specialty}, список оценок {self.list_estimates}'
#
#     def get_evaluation(self, estimation):
#         self.list_estimates.append(estimation)
#
#
# def average_ball(self):
#     count = 0
#     sr = 0
#     for i in self.list_estimates:
#         count += 1
#         sr += i
#     sr = sr / count
#     return sr
#
#
# st1 = Student("Иван", "Иванов", 1988, "програмист")
# st1.get_evaluation(5)
# st1.get_evaluation(4)
# st1.get_evaluation(3)
# print(st1)
# print(average_ball(st1))

#
# # 1.2
#
# class Book:
#     def __init__(self, named, autor, publication_year, genre, rating=0):
#         self.named = named
#         self.autor = autor
#         self.publication_year = publication_year
#         self.genre = genre
#         self.rating = rating
#
#     def __str__(self):
#         return f'Название: {self.named}, автор: {self.autor}, год издания: {self.publication_year}, жарр: {self.genre}, рейтинг: {self.rating}'
#
#     def __eq__(self, other):
#         if self.rating == other.rating:
#             return True
#         else:
#             return False
#
#     def __ne__(self, other):
#         if self.rating != other.rating:
#             return True
#         else:
#             return False
#
#     def __lt__(self, other):
#         if self.rating < other.rating:
#             return True
#         else:
#             return False
#
#     def __gt__(self, other):
#         if self.rating > other.rating:
#             return True
#         else:
#             return False
#
#     def get_rating(self, rating):
#         self.rating = rating
#         return self.rating
#
#
# b1 = Book('Синий трактор', "Котэ", 2018, 'приключения')
# b2 = Book('Колобок', "Дед да бабка", 1980, 'приключения')
#
# b1.get_rating(5.3)
# b2.get_rating(3)
# print(b1)
# print(b2)
# print(b1==b2)
# print(b1!=b2)
# print(b1<b2)
# print(b1>b2)
#
# 1.3
#
# class Car:
#     def __init__(self, brand, model, realese_year, color, mileage=0):
#         self.brand = brand
#         self.model = model
#         self.realise_year = realese_year
#         self. color = color
#         self.mileage = mileage
#
#     def __str__(self):
#         return f'Марка автомобиля {self.brand},модель {self.model}, год выпуска {self.realise_year}, \nцвет {self.color}, пробег {self.mileage}'
#
#     def new_mileage(self):
#         inp = int(input("Введите новый пробег в километрах"))
#         self.mileage = self.mileage + inp
#         return self.mileage
#
#     def __eq__(self, other):
#         if self.realise_year == other.realise_year:
#             return True
#         else:
#             return False
#
#     def __ne__(self, other):
#         if self.realise_year != other.realise_year:
#             return True
#         else:
#             return False
#
#     def __lt__(self, other):
#         if self.realise_year < other.realise_year:
#             return True
#         else:
#             return False
#
#     def __gt__(self, other):
#         if self.realise_year > other.realise_year:
#             return True
#         else:
#             return False
#
# # #Задание №2
# # #2.1
#
# class Animal:
#     def __init__(self, name, species, age):
#         self.name = name
#         self.species = species
#         self.age = age
#
#     def __str__(self):
#         return f'Имя животного {self.name}, вид животногот {self.species}, возраст {self.age}.'
#
#
#     def sound_animal(self, sound):
#         return f'{sound} издал(-а) звук {self.name}'
#
# a1 = Animal('корова', 'пятнистая', '4' )
# print(a1.sound_animal('muuu'))
# print(a1)
#
#
# # 2.2
#
# class Book:
#     def __init__(self, name, autor, number_pages):
#         self.name = name
#         self.autor = autor
#         self.number_pages  =number_pages
#
#     def __str__(self):
#         return  f"Название книги {self.name}, автор {self.autor}, количество страниц {self.number_pages}. "
#
#
#     def open_pages(self, other):
#         if other > self.number_pages:
#             return f"Книга не может быть открыта. В книге нет столько страниц!"
#         return f'Страница {other} открылась.'
#
#
# b1 = Book("Как кошки поработили людей", "кот Василий", 999)
#
# print(b1)
# print(b1.open_pages(11))
# print(b1.open_pages(9999))
#
#
# # 2.3
#
# class PassengerPlane:
#     def __init__(self, maker, model, passenger_capacity, current_height, current_speed):
#         self.maker = maker
#         self.model = model
#         self.passenger_capacity = passenger_capacity
#         self.current_height = current_height
#         self.current_speed = current_speed
#
#     def __str__(self):
#         return f'Производитель самолёта {self.maker}, модель {self.model}, вместимость пассажиров {self.passenger_capacity}, \nтекущая высота {self.current_height}, текущая скорость {self.current_speed}'
#
#     def takeoff(self):
#         print('Самолёт взлетел!')
#
#     def landing(self):
#         print('Самолёт приземлился!')
#
#     def current_height_(self, height):
#         self.current_height = height
#         return self.current_height
#
#     def current_sped_(self, speed):
#         self.current_speed = speed
#         return self.current_speed
#
# p1 = PassengerPlane('China', 'Vjuh', 101, 0, 0)
#
# print(p1)
# print(p1.takeoff())
# p1.current_height_(300)
# p1.current_sped_(100)
# print(p1)
# print(p1.landing())
#
#
## 2.4
#
# class MusicAlbum:
#     def __init__(self, musician, album_name, genre, list_track=None):
#         self.musician = musician
#         self.album_name = album_name
#         self.genre = genre
#         self.list_track = []
#
#     def __str__(self):
#         return f'Исполнитель {self.musician}, название альбома {self.album_name},\nжанр {self.genre}, список треков {self.list_track}.'
#
#     def add_track(self, track):
#         self.list_track.append(track)
#
#     def del_track(self, track):
#         self.list_track.remove(track)
#
#     def play_track(self, track):
#         print(f'Трек {track} воспроизведён.')
#
#
# m1 = MusicAlbum("Кот Кокос", "Мяу мяф", "новая музыка")
#
# print(m1)
# m1.add_track('дайте корм')
# m1.add_track("тыгыдык")
# print(m1)
# m1.del_track('дайте корм')
# print(m1)
#
#
# # Задание № 3.3
#
# class BankAccount:
#     def __init__(self, account, name, balance=0):
#         self.__account = account
#         self.__name = name
#         self.__balance = balance
#
#     def __str__(self):
#         return f"Номер счёта {self.__account}, имя владельца {self.__name}, баланс {self.__balance}."
#
#     def get_deposit_cash(self, cash):
#         if cash > 0:
#             self.__balance = self.__balance + cash
#             return self.__balance
#         else:
#             print('Проверьте правильность заполнения данных!')
#
#     def get_withdraw_cash(self, cash):
#         if  self.__balance > cash and cash > 0:
#             self.__balance = self.__balance - cash
#             return self.__balance
#         else:
#             print('Проверьте правильность заполнения данных!')
#
# b1 =BankAccount("12345", "Vitalson", 9999999)
# print(b1)
# print(b1.get_deposit_cash(111))
# print(b1)
# print(b1.get_withdraw_cash(888888))
# print(b1)
#
#
# # Задание № 3.4
#
# class Employee:
#     def __init__(self, name, post, salary):
#         self.__name = name
#         self.__post = post
#         self.__salary = salary
#
#     def __str__(self):
#         return f'Сотрудник по имени {self.__name}, на должности {self.__post}, получает зарплату в сумме {self.__salary} рублей.'
#
#     def get_salary_increase(self, cash):
#         if cash > 0 and cash <= 5000:
#             self.__salary = self.__salary + cash
#             return self.__salary
#         else:
#             print("Проверьте правильность заполнения данных ")
#
#
# emp1 = Employee('Иван', "менеджер", 10000)
# print(emp1)
# emp1.get_salary_increase(3000)
# print(emp1)
# emp1.get_salary_increase(6000)
# print(emp1)
#
#
# # Задание № 3.5
# from datetime import date
#
# class BankAccount:
#     def __init__(self, account_number , owner_name , balance, daily_withdrawal_limit):
#         self.__account_number  = account_number
#         self.__owner_name  = owner_name
#         self.__balance = balance
#         self.daily_withdrawal_limit = daily_withdrawal_limit
#         self.transactions = []
#
#     def __str__(self):
#         return f"Номер счёта {self.__account_number}, имя владельца {self.__owner_name }, \nбаланс {self.__balance}, дневной лимит снятия денег{self.daily_withdrawal_limit}."
#
#     def get_deposit(self, cash):
#         if cash > 0:
#             self.__balance = self.__balance + cash
#             dt_now = date.today()
#             self.transactions.append(f'{dt_now} Изменение счёта: +{cash}')
#             return self.transactions
#         else:
#             print('Проверьте правильность заполнения данных!')
#
#     def get_withdraw(self, cash):
#         if cash > 0 and cash <= self.daily_withdrawal_limit:
#             self.daily_withdrawal_limit = self.daily_withdrawal_limit - cash
#             dt_now = date.today()
#             self.transactions.append(f'{dt_now} Изменение счёта: -{cash}')
#
#             if  self.__balance > cash and cash > 0:
#                 self.__balance = self.__balance - cash
#                 return self.transactions
#         else:
#             print('Проверьте правильность заполнения данных!')
#
#     def display_account_info(self):
#         return f'Номер счёта {self.__account_number}, имя владельца {self.__owner_name}, \nтекущий баланс {self.__balance}'
#
#     def display_transaction_history(self):
#         return self.transactions
#
#
# b1 = BankAccount('12345', 'Иван', 10000, 5000)
# print(b1)
# b1.get_deposit(3000)
# print(b1.display_account_info())
# b1.get_deposit(2000)
# print(b1.display_account_info())
# b1.get_withdraw(200)
# b1.get_withdraw(4000)
# print(b1.display_transaction_history())
#
#
# # Задание № 3.6
#
class Event:
    def __init__(self, event_id, name, date, tickets_count, tickets, t):
        self.event_id = event_id
        self.name = name
        self.date = date
        self.tickets_count = tickets_count
        self.tickets = tickets
        self.t = t

    def __str__(self):
        return f'Уникальный идентификатор {self.event_id}, название мероприятия {self.name},\nдата проведения мероприятия {self.date}'

    def add_ticket(self, ticket):
        pass

    def remove_tickket(self, ticket_id):
        pass

    def display_event_info(self):
        pass


class Ticket:
    def __init__(self, ticket_id, event_id, price, seat=None):
        self.ticket_id = ticket_id
        self.event_id = event_id
        self.price = price
        self.seat = seat

    def display_ticket_info(self):
        return f'Уникальный идентфикатор {self.ticket_id}, идентификатор мероприятия {self.event_id}, \nцена билета {self.price}, место проведения {self.seat}'


t = Ticket('001', '12345', 100, 'small hall')
e = Event('12345', 'balet', '10.10.2020', '5', t)


print(e)

#
# class Worker:
#     def __init__(self, full_name):
#         self.__full_name = full_name
#
#     def get_full_name(self) -> str:
#         return self.__full_name
#
#     def feed_animal(self, animal) -> bool:
#         if animal.get_is_fed():
#             return False
#         animal.set_is_fed(True)
#         return True
#
# class Animal:
#      def __init__(self, name):
#          self.__name = name
#          self.__is_fed = False
#
#      def get_name(self) -> str:
#          return self.__name
#
#      def get_is_fed(self) -> bool:
#          return self.__is_fed
#          self.__active_time()
#      def set_is_fed(self, status: bool) :
#         self.__is_fed = status
#
#         if self.__is_fed:
#             self.__active_time()
#
#
#      def __active_time(self) -> None:
#          pass
#
# class Timer:
#     pass
#
# a1 = Animal('Kot')
# w1 = Worker("Ivan Ibn Hattab")
# print(w1.feed_animal(a1))