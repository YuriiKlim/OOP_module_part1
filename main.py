def add(x, y):
    return x + y

result1 = add(1, 4)
result2 = add("Hello", "World")
print(result1)
print(result2)

# Динамічний поліморфізм

class Animal:
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        return "Bark!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"
def animal_make_sound(animal):
    return animal.make_sound()

dog, cat, = Dog(), Cat()
result1 = animal_make_sound(dog)
result2 = animal_make_sound(cat)
print(result1, result2)