# Завдання 2
# Створіть клас Ship, який містить інформацію про кораблі.
# За допомогою механізму успадкування реалізуйте клас
# Frigate (містить інформацію про фрегат), клас Destroyer(містить
# інформацію про есмінця), клас Cruiser (містить інформацію
# про крейсер).
# Кожен із класів має містити необхідні для роботи методи.
class Ship:
    def __init__(self, name, year_built, speed, weight):
        self._name = name
        self._year_built = year_built
        self._speed = speed
        self._weigth = weight

    def describe_ship(self):
        print(f"{self._name}, Збудований у {self._year_built} році, швидкість: {self._speed}км/год, Вага: {self._weigth} тонн")


class Frigate(Ship):
    def __init__(self, name, year_built, speed, weight, armament):
        super().__init__(name, year_built, speed, weight)
        self.armament = armament

    def describe_armament(self):
        print(f"{self._name} Озброєний: {self.armament}.")


class Destroyer(Ship):
    def __init__(self, name, year_built, speed, weight, bridge_destroyer):
        super().__init__(name, year_built, speed, weight)
        self.bridge_destroyer = bridge_destroyer

    def is_bridge_destroyer(self):
        print(f"{self._name} Може влупити по кримському мосту? {self.bridge_destroyer}")


class Cruiser(Ship):
    def __init__(self, name, year_built, speed, weight, capacity):
        super().__init__(name, year_built, speed, weight)
        self.capacity = capacity

    def describe_capacity(self):
        print(f"{self._name} може вмістити {self.capacity} тонн.")


frigate = Frigate("Гетьман Сагайдачний", 1997, 40, 10500, "Зенітка")
destroyer = Destroyer("Батько Бандера", 2013, 60, 16800, "Так")
cruiser = Cruiser("Тернопіль", 2002, 55, 21900, 9600)


frigate.describe_ship()
frigate.describe_armament()

destroyer.describe_ship()
destroyer.is_bridge_destroyer()

cruiser.describe_ship()
cruiser.describe_capacity()
