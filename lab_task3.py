# Завдання 3
# Створіть клас "Електронний Гаманець" додавши
# можливість видаляти та додавати гроші, а також перевіряти
# баланс.
class ElectronicWallet:
    def __init__(self):
        self.__balance = 0.0

    def add_money(self, amount):
        """Додати гроші"""
        if amount > 0:
            self.__balance += amount
            print(f"{amount} грн успішно додано до гаманця.")
        else:
            print("Сума для додавання має бути більше нуля.")

    def withdraw_money(self, amount):
        """Вивести гроші"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} грн успішно виведено з гаманця.")
        else:
            print("Недостатньо коштів у гаманці або некоректна сума.")

    def check_balance(self):
        """Перевірити баланс"""
        print(f"Баланс гаманця: {self.__balance} грн")

wallet = ElectronicWallet()

wallet.add_money(500)
wallet.check_balance()

wallet.withdraw_money(200)
wallet.check_balance()

wallet.withdraw_money(1000)
