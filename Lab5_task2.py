# Завдання 2
# Створіть клас Passport (паспорт), який міститиме
# паспортну інформацію про громадянина заданої країни.
# За допомогою механізму успадкування реалізуйте
# клас ForeignPassport (закордонний паспорт), похідний
# від Passport.
# Нагадаємо, що закордонний паспорт містить, крім
# паспортних даних, дані про візи і номер закордонного
# паспорта.
# Кожен із класів має містити необхідні методи
class Passport:
    def __init__(self, name, surname, passport_number):
        self._name = name
        self._surname = surname
        self._passport_number = passport_number

    def get_info(self):
        print(f"Ім'я: {self._name}, Прізвище: {self._surname}, Номер паспорта: {self._passport_number}")


class ForeignPassport(Passport):
    def __init__(self, name, surname, passport_number, foreign_passport_number, visas=[]):
        super().__init__(name, surname, passport_number)
        self._foreign_passport_number = foreign_passport_number
        self._visas = visas

    def get_info(self):
        super().get_info()
        print(f"Номер закордонного паспорта: {self._foreign_passport_number}, Візи: {', '.join(self._visas)}")

    def set_visa(self, visa):
        self._visas.append(visa)


passport = Passport("Юрій", "Клім", "AA123456")


foreign_passport = ForeignPassport("Юрій", "Клім", "AA123456", "FP654321", ["Канада", "Великобританія"])


foreign_passport.set_visa("США")
foreign_passport.get_info()
