# Завдання 3
# Створіть базовий клас «Тварина» та похідні класи:
# «Тигр», «Крокодил», «Кенгуру». Встановіть за допомогою
# конструктора ім’я кожної тварини та її характеристики.
# Створіть для кожного класу необхідні методи та поля.
class Animal:
    def __init__(self, name, age, breed):
        self._name = name
        self._age = age
        self._breed = breed

    def get_info(self):
        print(f"Тварина: {self._name}, Вік: {self._age}, Вид: {self._breed}")


class Tiger(Animal):
    def __init__(self, name, age, breed, speed):
        super().__init__(name, age, breed)
        self._speed = speed

    def get_info(self):
        super().get_info()
        print(f"Тип: Тигр, Швидкість: {self._speed} км/год")


class Crocodile(Animal):
    def __init__(self, name, age, breed, length):
        super().__init__(name, age, breed)
        self._length = length

    def get_info(self):
        super().get_info()
        print(f"Тип: Крокодил, Довжина: {self._length} м")


class Kangaroo(Animal):
    def __init__(self, name, age, breed, jump_length):
        super().__init__(name, age, breed)
        self._jump_length = jump_length

    def get_info(self):
        super().get_info()
        print(f"Тип: Кенгуру, Довжина стрибка: {self._jump_length} м")


tiger = Tiger("Тигр Юлі Тимошенко", 15,"Білий", 60)
crocodile = Crocodile("Крок", 7, "Африканський", 3)
kangaroo = Kangaroo("Джек", 12, "Австралійський", 6)


tiger.get_info()
crocodile.get_info()
kangaroo.get_info()
