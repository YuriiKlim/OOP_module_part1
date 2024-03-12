class Dogs():
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed


# створення екземпляру класу
my_dog = Dogs("Пес", 5, "хаскі")
print(my_dog.name)
print(my_dog.age)
print(my_dog.breed)
