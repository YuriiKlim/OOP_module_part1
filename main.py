# Інкапсуляція
# class Myclass:
#     def publick_method1(self):
#         print("hello")
#     def publick_method2(self):
#         print("hello from method2")
#         self.publick_method1()
# obj = Myclass()
# obj.publick_method2()
#
# class Myclass_privat:
#     def __init__(self):
#         self.attribute = 20  #public
#         self._attribute = 10 #private
#     def get_attribute(self):
#         return self._attribute
#
# obj = Myclass_privat()
# print(f"{obj._attribute=}")
# print(f"{obj.get_attribute()=}")
#
# class Myclass_full_privat:
#     def __init__(self):
#         self.attribute = 20  #public
#         self.__attribute = 100 #private
#     def get_attribute(self):
#         return self.__attribute
#     def set_attribute(self, value):
#         self.__attribute
#
# obj = Myclass_full_privat()
# print(f"{obj._Myclass_full_privat__attribute=}")

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
#     def get_balance(self):
#         return self.__balance
#     def deposit(self, amount):
#         self.__balance += amount
#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("no money=(")
#
# account = BankAccount(100)
# print(account.get_balance())
# account.deposit(60)
# print(account.get_balance())
# account.withdraw(80)
# account.withdraw(200)
# print(account.get_balance())

# class Apartment:
#     def __init__(self, num_rooms, area):
#         self.__num_rooms = num_rooms
#         self.__area = area
#
#     def get_num_rooms(self):
#         return self.__num_rooms
#     def get_area(self):
#         return self.__area
#
# apartment = Apartment(4,80)
# print(f"rooms in apartments - {apartment.get_num_rooms()}")
# print(f"area in apartments - {apartment.get_area()}")

class Event:
    count = 0

    def __init__(self, name=None, date=None, desc=None):
        self.__name = name
        self.__date = date
        self.__desc = desc
        Event.count += 1
    def set_date(self, new_date):
        self.__date = new_date
    def set_desc(self,new_desc):
        self.__desc = new_desc
    def get_name(self):
        return self.__name
    def get_date(self):
        return self.__date
    def get_desc(self):
        return self.__desc
    def __del__(self):
        Event.count -= 1
        del self
event1 = Event()
event2 = Event()
event3 = Event()

print(Event.count, event1.count)
del event3
print(Event.count, event1.count)