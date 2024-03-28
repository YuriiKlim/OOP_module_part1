# Завдання 4
# Створіть базовий клас Employer (службовець) з функцією Print(). Функція має виводити інформацію про службовця. Для базового класу це може бути рядок із написом
# «This is Employer class».
# Створіть від нього три похідні класи: President, Manager, Worker. Перевизначте функцію Print() для виведення
# інформації, що відповідає кожному типу службовця.
class Employer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}. {self.job()}"

    def __int__(self):
        return self.age

    def job(self):
        return "Робить вигляд роботи"


class President(Employer):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __str__(self):
        return "President: " + self.name + ", Age: " + str(self.age) + " - " + self.job()

    def job(self):
        return "Керує"


class Manager(Employer):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __str__(self):
        return "Manager: " + self.name + ", Age: " + str(self.age) + " - " + self.job()

    def job(self):
        return "Менеджерить"


class Worker(Employer):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __str__(self):
        return "Worker: " + self.name + ", Age: " + str(self.age) + " - " + self.job()

    def job(self):
        return "Професійно робить вигляд роботи"


president = President("Юрій", 55)
manager = Manager("Юлія", 40)
worker = Worker("Володя", 30)


print(president)
print(manager)
print(worker)


print(int(president))


