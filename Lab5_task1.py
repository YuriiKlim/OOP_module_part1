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
        self._specialization = specialization

    def get_info(self):
        super().get_info()
        print(f"Спеціалізація: {self._specialization}")


class Sailor(Human):
    def __init__(self, name, age, citizenship, ship):
        super().__init__(name, age, citizenship)
        self._ship = ship

    def get_info(self):
        super().get_info()
        print(f"Корабель: {self._ship}")


class Pilot(Human):
    def __init__(self, name, age, citizenship, aircraft):
        super().__init__(name, age, citizenship)
        self._aircraft = aircraft

    def get_info(self):
        super().get_info()
        print(f"Тип літака: {self._aircraft}")


builder = Builder("Іван", 35, "Українець", "муляр")
sailor = Sailor("Петро", 29, "Українець", "Aurora")
pilot = Pilot("Олексій", 41, "Українець", "Boeing 737")

builder.get_info()
sailor.get_info()
pilot.get_info()
