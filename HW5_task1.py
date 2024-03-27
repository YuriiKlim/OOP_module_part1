# Завдання 1
# Створіть клас Device, який містить інформацію про пристрій.
# За допомогою механізму успадкування реалізуйте клас
# Coffee Machine (містить інформацію про кавомашину), клас
# Blender (містить інформацію про блендер), клас MeatGrinder
# (містить інформацію про м’ясорубку).
# Кожен із класів має містити необхідні для роботи методи.
class Device:
    def __init__(self, name, power):
        self._name = name
        self._power = power

    def turn_on(self):
        print(f"{self._name} is now on, consuming {self._power} watts.")

    def turn_off(self):
        print(f"{self._name} is now off.")


class CoffeeMachine(Device):
    def __init__(self, name, power, coffee_type):
        super().__init__(name, power)
        self.coffee_type = coffee_type

    def make_coffee(self):
        print(f"Making {self.coffee_type} coffee... Enjoy your drink!")


class Blender(Device):
    def __init__(self, name, power, speed):
        super().__init__(name, power)
        self.speed = speed

    def blend(self):
        print(f"Blending at speed {self.speed}... Your blend is ready!")


class MeatGrinder(Device):
    def __init__(self, name, power, capacity):
        super().__init__(name, power)
        self.capacity = capacity

    def grind_meat(self):
        print(f"Grinding meat with capacity {self.capacity}... Your meat is ground!")


coffee_machine = CoffeeMachine("Espresso Maker", 800, "Espresso")
blender = Blender("Super Blender", 500, "High")
meat_grinder = MeatGrinder("Ultimate Grinder", 1000, "2kg")


coffee_machine.turn_on()
coffee_machine.make_coffee()
coffee_machine.turn_off()

blender.turn_on()
blender.blend()
blender.turn_off()

meat_grinder.turn_on()
meat_grinder.grind_meat()
meat_grinder.turn_off()
