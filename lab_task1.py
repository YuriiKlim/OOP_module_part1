# Завдання 1
# Створіть клас "Користувач" з атрибутами "ім'я", "вік" та
# "email". Застосуйте інкапсуляцію, щоб забезпечити, що ці
# дані можна отримати лише через методи класу.
class User:
    def __init__(self, name, age, email):
        self.__name = name
        self.__age = age
        self.__email = email
    def get_name(self):
        return self.__name
    def set_name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            print("Некоректне ім'я.")
    def get_age(self):
        return self.__age
    def set_age(self, value):
        if isinstance(value, int) and 0 < value < 150:
            self.__age = value
        else:
            print("Некоректний вік.")
    def get_email(self):
        return self.__email
    def set_email(self, value):
        if "@" in value and "." in value:
            self.__email = value
        else:
            print("Некоректна email адреса.")
user = User("Юрій", 30, "Yurii@gmail.com")

print(f"Ім'я: {user.get_name()}")
print(f"Вік: {user.get_age()}")
print(f"Email: {user.get_email()}")

user.set_name("Анна")
user.set_age(25)
user.set_email("anna@gmail.com")

user.set_age(-5)
user.set_email("aaaaaaa")
print(f"\nОновлені дані:")
print(f"Ім'я: {user.get_name()}")
print(f"Вік: {user.get_age()}")
print(f"Email: {user.get_email()}")

