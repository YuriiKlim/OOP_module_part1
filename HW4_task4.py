# Завдання 4
#  Створіть клас InformationSystem, який має атрибут data
# - словник, де ключі - це імена користувачів, а значення -
# список їх контактів. Реалізуйте методи класу для додавання
# нових користувачів та їх контактів.
class InformationSystem:
    def __init__(self):
        self.data = {}

    @staticmethod
    def input_alpha_data(prompt):
        while True:
            value = input(prompt).lower()
            if value.replace(' ', '').isalpha():
                return value
            else:
                print("Неправильне значення. Будь ласка, введіть лише букви.")

    def add_user(self):
        user_name = self.input_alpha_data("Введіть ім'я користувача: ")
        if user_name not in self.data:
            self.data[user_name] = []
            print(f"Користувача {user_name} успішно додано.")
        else:
            print(f"Користувач {user_name} вже існує.")

    def display_users(self):
        if self.data:
            print("Список користувачів та їх контакти:")
            for i, (user, contacts) in enumerate(self.data.items(), 1):
                print(f"{i}. {user}: {', '.join(contacts) if contacts else 'Немає контактів'}")
        else:
            print("Список користувачів порожній.")

    def select_user(self):
        self.display_users()
        if not self.data:
            return
        try:
            choice = int(input("Виберіть номер користувача: ")) - 1
            user_name = list(self.data.keys())[choice]
            self.user_menu(user_name)
        except (ValueError, IndexError):
            print("Невірний вибір. Спробуйте ще раз.")

    def add_contact(self, user_name):
        contact = self.input_alpha_data("Введіть ім'я контакта: ")
        self.data[user_name].append(contact)
        print("Контакт додано.")

    def delete_contact(self, user_name):
        if not self.data[user_name]:
            print("У користувача немає контактів.")
            return
        for i, contact in enumerate(self.data[user_name], 1):
            print(f"{i}. {contact}")
        try:
            choice = int(input("Виберіть контакт для видалення: ")) - 1
            del self.data[user_name][choice]
            print("Контакт видалено.")
        except (ValueError, IndexError):
            print("Невірний вибір. Спробуйте ще раз.")

    def user_menu(self, user_name):
        while True:
            print(f"\nКористувач: {user_name}")
            print("1. Додати контакти\n2. Видалити контакти\nenter - Повернутися до головного меню")
            choice = input("Ваш вибір: ")
            if choice == "1":
                self.add_contact(user_name)
            elif choice == "2":
                self.delete_contact(user_name)
            elif choice == "":
                break
            else:
                print("Невідома опція. Спробуйте ще раз.")

    def run(self):
        while True:
            print("\nСистема управління користувачами")
            print("1. Відобразити користувачів\n2. Додати нового користувача\n3. Вибрати користувача\nenter - Вийти")
            choice = input("Введіть ваш вибір: ")
            if choice == "1":
                self.display_users()
            elif choice == "2":
                self.add_user()
            elif choice == "3":
                self.select_user()
            elif choice == "":
                print("Вихід з програми.")
                break
            else:
                print("Невідома опція. Спробуйте ще раз.")

if __name__ == "__main__":
    info_system = InformationSystem()
    info_system.run()


