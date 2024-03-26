class Animal:
    def sound(self):
        print("Some sound: hrrr")

    def make_noise(self):
        self.sound()
        self.sound()
        self.sound()


class Dog(Animal):
    def run(self):
        print('dog is running')

    def sound(self):
        print("Hav, hav")


class Cat(Animal):
    def sound(self):
        super().sound()
        print("Miau")

    def get_super(self):
        print(super())


# obj = Dog()
# print(obj.sound())
# print()
# obj.make_noise()

#cat = Cat()
#cat.sound()

class Figure:
    def __init__(self, area):
        self._area = area
        print('init from Figure')


class Circle(Figure):
    def __init__(self, area, radius):
        super().__init__(area)
        self._radius = radius

        print('init from Circle')

    def print_info(self):
        print(f'{self._area=}')
        print(f'{self._radius=}')


obj = Circle(20, 3)
obj.print_info()


class Person:
    def __init__(self, name, age, gender):
        self._name = name
        self._age = age
        self._gender = gender

    def get_name(self):
        return self._name


class Student(Person):
    def __init__(self, name, age, gender, student_id):
        super().__init__(name, age, gender)
        self._student_id = student_id

    def get_id(self):
        return self._student_id

    def set_id(self, new_id):
        self._student_id = new_id

    def get_info(self, objects):
        print(f'Студент {self._name} вивчає:')

        for i, object in enumerate(objects):
            print(f'{i+1}. {object}')
        '''
        for i in range(len(objects)):
            object = objects[i]
        '''


class Teacher(Person):
    def __init__(self, name, age, gender, employee_id):
        super().__init__(name, age, gender)
        self._employee_id = employee_id
        self._students = []

    def get_id(self):
        return self._employee_id

    def set_id(self, new_id):
        self._employee_id = new_id

    def add_student(self, student:Student):
        self._students.append(student)

    def add_grade(self, grade):
        for student in self._students:
            print(f'{student.get_name()} отримав {grade}')


student1 = Student('John', 27, 'male', '00012345')
student2 = Student('Mike', 27, 'male', '00012345')

#student.get_info(['Math', 'Python', 'C++'])
teacher = Teacher('Anna', 35, 'female', '999789456')
teacher.add_student(student1)
teacher.add_student(student2)

teacher.add_grade(12)


class Product:
    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self._quantity = quantity


class CD(Product):
    def __init__(self, name, price, quantity, singer, num_songs):
        super().__init__(name, price, quantity)
        self._singer = singer
        self._num_songs = num_songs

    def get_singer(self):
        return self._singer

    def set_singer(self, new_singer):
        self._singer = new_singer

    def get_num_songs(self):
        return self._num_songs

    def set_num_songs(self, new_num_songs):
        self._num_songs = new_num_songs


class MusicalInstrument(Product):
    def __init__(self, name, price, quantity, instrument_type, material):
        super().__init__(name, price, quantity)
        self._type = instrument_type
        self._material = material


cd = CD('CD_name', 200, 1, "Elsa`s Ocean", 10)
print(cd.get_singer())