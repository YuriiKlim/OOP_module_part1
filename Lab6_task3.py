# Завдання 4
# Створіть базовий клас Employer (службовець) з функцією Print(). Функція має виводити інформацію про службовця. Для базового класу це може бути рядок із написом
# «This is Employer class».
# Створіть від нього три похідні класи: President, Manager, Worker. Перевизначте функцію Print() для виведення
# інформації, що відповідає кожному типу службовця.
class Employer:
    def __init__(self, age=0):
        self.age = age

    def __str__(self):
        return "This is Employer class"

    def __int__(self):
        return self.age


class President(Employer):
    def __str__(self):
        return "This is President class"


class Manager(Employer):
    def __str__(self):
        return "This is Manager class"


class Worker(Employer):
    def __str__(self):
        return "This is Worker class"


employer = Employer(50)
president = President(45)
manager = Manager(40)
worker = Worker(35)


print(employer)
print(int(employer))

print(president)
print(int(president))

print(manager)
print(int(manager))

print(worker)
print(int(worker))

