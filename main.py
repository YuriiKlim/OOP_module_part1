#перевантаження методів
class String_manipulator:
    def concatenate(self, a, b):
        return a + b

    def concatenate_str(self, a, b):
        return str(a) + str(b)

calc = String_manipulator()
print(calc.concatenate(2,3))
print(calc.concatenate_str("Hey","Dude"))