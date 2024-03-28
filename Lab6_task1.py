# Завдання 2
# Використовуючи механізм множинного успадкування, створіть клас «Автомобіль». Також мають бути класи:
# «Колеса», «Двигун», «Двері» та ін.
class Wheels:
    def __init__(self, wheels_type):
        self.wheels_type = wheels_type

    def wheel_info(self):
        return f"Тип резини: {self.wheels_type}"


class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def engine_info(self):
        return f"Тип двигуна: {self.engine_type}"


class Doors:
    def __init__(self, number_of_doors):
        self.number_of_doors = number_of_doors

    def doors_info(self):
        return f"Кількість дверей: {self.number_of_doors}"


class Car(Wheels, Engine, Doors):
    def __init__(self, model, wheels_type, engine_type, number_of_doors):
        Wheels.__init__(self, wheels_type)
        Engine.__init__(self, engine_type)
        Doors.__init__(self, number_of_doors)
        self.model = model

    def car_info(self):
        return (f"Модель автомобіля: {self.model}\n" +
                self.wheel_info() + "\n" +
                self.engine_info() + "\n" +
                self.doors_info())


my_car = Car("Toyota Camry", "Літні", "Бензиновий", 4)
print(my_car.car_info())
