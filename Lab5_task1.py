# Завдання 1
# Створіть клас Human, який міститиме інформацію
# про людину.
# За допомогою механізму успадкування реалізуйте
# клас Builder (містить інформацію про будівельника),
# клас Sailor (містить інформацію про моряка), клас Pilot
# (містить інформацію про льотчика).
# Кожен із класів має містити необхідні для роботи
# методи.
class Human:
    def __init__(self, name, age, citizenship):
        self._name = name
        self._age = age
        self._citizenship = citizenship

    def get_info(self):
        print(f"Ім'я: {self._name}, Вік: {self._age}, Громадянство: {self._citizenship}")

class Builder(Human):
    def __init__(self, name, age, citizenship, specialization):
        super().__init__(name, age, citizenship)
        self.specialization = specialization

    def get_info(self):
        super().get_info()
        print(f"Спеціалізація: {self.specialization}")

class Sailor(Human):
    def __init__(self, name, age, citizenship, ship):
        super().__init__(name, age, citizenship)
        self.ship = ship

    def get_info(self):
        super().get_info()
        print(f"Корабель: {self.ship}")

class Pilot(Human):
    def __init__(self, name, age, citizenship, aircraft_type):
        super().__init__(name, age, citizenship)
        self.aircraft_type = aircraft_type

    def get_info(self):
        super().get_info()
        print(f"Тип літака: {self.aircraft_type}")


builder = Builder("Іван", 35, "Українець", "муляр")
sailor = Sailor("Петро", 29, "Українець", "Aurora")
pilot = Pilot("Олексій", 41, "Українець", "Boeing 737")

builder.get_info()
sailor.get_info()
pilot.get_info()
