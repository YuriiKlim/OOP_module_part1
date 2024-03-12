# Завдання 5
# Створіть клас BankAccount з атрибутами balance
# та owner, а також методами deposit та withdraw для
# здійснення операцій з балансом. Реалізуйте перевірку
# на те, що баланс не може стати від'ємним.
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Внесено {amount}. Поточний баланс: {self.balance}")
        else:
            print("Сума внесення має бути більшою за нуль.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Виведено {amount}. Поточний баланс: {self.balance}")
        elif amount > self.balance:
            print("Недостатньо коштів на рахунку.")
        else:
            print("Сума виведення має бути більшою за нуль.")

account = BankAccount("Юра Клім", 1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(1500)
