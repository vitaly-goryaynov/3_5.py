class Educational_institution:
    def __init__(self, name:str, typ:str, address:str, count_students:int, count_teacher:int):
        self._name = name
        self._typ = typ
        self._address  = address
        self._count_students = count_students
        self._count_teacher = count_teacher


    def info(self) -> None:
        print(f'''Название {self._name},
тип учебного заведения {self._typ},
адрес {self._address},
количество студентов {self._count_students},
количество учетилей {self._count_teacher}''')


    def set_count_students(self, new_count: int) -> None:
        if new_count > 0:
            self.count_students = new_count

    def get_count_students(self) -> int:
        return self._count_students

    def add_new_teacher(self) -> None:
        self._count_teacher += 1

    def get_count_teacher(self) -> int:
        return self._count_teacher


class University(Educational_institution):
    def __init__(self, name:str, typ:str, address:str, count_students:int, count_teacher:int, level_accreditation:int):
        Educational_institution.__init__(self, name, typ, address, count_students, count_teacher)
        self._list_faculty = []
        self._level_accreditation = level_accreditation

    def info (self) -> None:
        super().info()
        print(f'Список факультетов {self._list_faculty}, \nуровень аккредитации {self._level_accreditation}')

    def add_faculty(self, faculty:str) -> None:
        if not faculty in self._list_faculty:
            self._list_faculty.append(faculty)

    def get_list_faculty(self) -> list:
        return self._list_faculty

    def set_level_accreditation(self, new_level:int) -> None:
        self._level_accreditation = new_level

    def get_level_accreditation(self) -> int:
        return self._level_accreditation


u1 = University('Зелёный шум', "школа", "Волжский", 200, 10, 3)
u1.add_faculty('математический')
u1.info()