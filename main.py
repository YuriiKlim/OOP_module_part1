class Animals:
    def breath(self):
        print("дихає")
    def move(self):
        print("рухається")
    def eat(self):
        print("їсть")

class Dogs(Animals):
    pass

class Cats(Animals):
    pass

# створення екземпляру класу
my_dog = Dogs()
my_dog.breath()
my_dog.move()
my_dog.eat()
