# class Bank:
#     count = 0
#     exchange_rate_usd_uah = 38
#     def __init__(self):
#         self.balance = 10
#
#     def greet(self):
#         print("Hello")
#
#     @staticmethod
#     def uah_to_usd(value_uah):
#         print(Bank.exchange_rate_usd_uah)
#         return  value_uah / 38
#
#     @classmethod
#     def uah_to_usd2(cls, value_uah):
#         return  value_uah / cls.exchange_rate_usd_uah
#
#     def set_balance(self, balance):
#         self.balance = balance
#
#     @classmethod
#     def get_count(cls):
#         return cls.count
#
#     def get_exchange_rate(cls):
#
# object1 = Bank()
# print(object1.uah_to_usd(1000))
#

#2

class Calculator:
    @staticmethod
    def add_numbers(num1, num2):
        return num1 + num2

    @classmethod
    def add_numbers_with_round(cls,num1, num2):
        num1 = round(num1)
        num2 = round(num2)
        return cls.add_numbers(num1, num2)


print(Calculator.add_numbers(5, 9))
print(Calculator.add_numbers_with_round(1.4, 5.075))