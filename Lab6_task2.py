# Завдання 3
# Створіть базовий клас «Домашня тварина» та похідні
# класи «Пес», «Кіт», «Папуга», «Хом’як». За допомогою
# конструктора встановіть ім’я кожної тварини та її характеристики. Реалізуйте для кожного із класів наступні
# методи:
# ■ Sound — видає звук тварини (пишемо текстом в консоль);
# ■ Show — відображає ім’я тварини;
# ■ Type — відображає підвид тварини.
class Pet:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass

    def show(self):
        print(f"Ім'я {__class__.__name__}: {self.name}")

    def type(self):
        pass


class Dog(Pet):
    def sound(self):
        return "Гав"

    def type(self):
        return "Пес"

    def subtype(self):
        return "Алабай"


class Cat(Pet):
    def sound(self):
        return "Мяу"

    def type(self):
        return "Кіт"

    def subtype(self):
        return "Сфінкс"


class Parrot(Pet):
    def sound(self):
        return "Привіт"

    def type(self):
        return "Папуга"

    def subtype(self):
        return "Хвилястий"


class Hamster(Pet):
    def sound(self):
        return "Писк"

    def type(self):
        return "Хом'як"

    def subtype(self):
        return "Карликовий"


dog = Dog("Кураж")
cat = Cat("Том")
parrot = Parrot("Володя")
hamster = Hamster("Джері")


pets = [dog, cat, parrot, hamster]
for pet in pets:
    pet.show()
    print(f"Звук: {pet.sound()}")
    print(f"Тип: {pet.type()}")
    print(f"Підтип: {pet.subtype()}\n")
