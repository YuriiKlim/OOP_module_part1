class Duck:
    def quack(self):
        print("Кря!")

class Person:
    def quack(self):
        print("не той кря")

def make_it_quack(obj):
    obj.quack()

duck = Duck()
person = Person()
make_it_quack(duck)
make_it_quack(person)