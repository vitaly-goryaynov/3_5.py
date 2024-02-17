# # 3.7.2
# class Educational_institution:
#     def __init__(self, name:str, typ:str, address:str, count_students:int, count_teacher:int):
#         self._name = name
#         self._typ = typ
#         self._address  = address
#         self._count_students = count_students
#         self._count_teacher = count_teacher
#
#
#     def info(self) -> None:
#         print(f'''Название {self._name},
# тип учебного заведения {self._typ},
# адрес {self._address},
# количество студентов {self._count_students},
# количество учетилей {self._count_teacher}''')
#
#
#     def set_count_students(self, new_count: int) -> None:
#         if new_count > 0:
#             self.count_students = new_count
#
#     def get_count_students(self) -> int:
#         return self._count_students
#
#     def add_new_teacher(self) -> None:
#         self._count_teacher += 1
#
#     def get_count_teacher(self) -> int:
#         return self._count_teacher
#
#
# class University(Educational_institution):
#     def __init__(self, name:str, typ:str, address:str, count_students:int, count_teacher:int, level_accreditation:int):
#         Educational_institution.__init__(self, name, typ, address, count_students, count_teacher)
#         self._list_faculty = []
#         self._level_accreditation = level_accreditation
#
#     def info (self) -> None:
#         super().info()
#         print(f'Список факультетов {self._list_faculty}, \nуровень аккредитации {self._level_accreditation}')
#
#     def add_faculty(self, faculty:str) -> None:
#         if not faculty in self._list_faculty:
#             self._list_faculty.append(faculty)
#
#     def get_list_faculty(self) -> list:
#         return self._list_faculty
#
#     def set_level_accreditation(self, new_level:int) -> None:
#         self._level_accreditation = new_level
#
#     def get_level_accreditation(self) -> int:
#         return self._level_accreditation
#
#
# u1 = University('Зелёный шум', "школа", "Волжский", 200, 10, 3)
# u1.add_faculty('математический')
# u1.info()
#

# 7.3

class Empoloyee:
    def __init__(self, name:str, post:str, departament:str, salary:float, work_experience:int):
        self._name = name
        self._post = post
        self._departament = departament
        self._salary = salary
        self._work_experience = work_experience

    def info(self):
        print(f'''Имя сотрудника {self._name},
должность {self._post},
отдел {self._departament},
зарплата {self._salary},
стаж работы {self._work_experience}''')

    def increase_percentage_salary(self, percent:float) -> None:
        if self._salary > 0 and percent > 0:
            self._salary += (self._salary / 100 * percent)
        else:
            print('Проверьте правильность заполнения данных')

    def  get_salary(self) -> float:
        return self._salary

    def set_new_post(self, new_post:str):
        self._post = new_post

    def get_post(self) -> str:
        return self._post


class Manager(Empoloyee):
    def __init__(self, name:str, post:str, departament:str, salary:float, work_experience:int, count_project:int):
        Empoloyee.__init__(self, name, post, departament, salary, work_experience)
        self._list_employee = []
        self._count_project = count_project


    def info(self):
        super().info()
        print(f'Список подчинённых: {self._list_employee}, \nколичество проектов {self._count_project}')

    def add_employee_in_list(self, employee:object) -> None:
        if employee in self._list_employee:
            print('Работник уже есть в списке')
        if not employee in self._list_employee:
            self._list_employee.append(employee)
            print('Работник добавлен в список')


    def get_employee_list(self) -> list:
        return self._list_employee

    def delete_employee_in_list(self, employee:object):
        if not employee in self._list_employee:
            print('Работника нет в списке')
        else:
            self._list_employee.remove(employee)

m1 = Manager('Василий', 'менеджер', "подаж", 50000, 3, 2)
m2 = Manager('Василий', 'менеджер', "подаж", 50000, 3, 2)
m1.add_employee_in_list(m1)
m1.add_employee_in_list(m2)
m1.increase_percentage_salary(5)

m1.info()
print(*m1.get_employee_list())