# Завдання 5
# Створіть клас Character, який має атрибути name, health
# та damage. Реалізуйте метод класу attack, який виводить
# повідомлення про атаку гравця.
class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, target):
        print(f"{self.name} атакує {target.name} і завдає {self.damage} пошкоджень.")
        current_heal = target.health - self.damage
        print(f"У {target.name} залишається {current_heal} здоров'я")

# Приклад використання:
character1 = Character("Герой", 100, 20)
character2 = Character("Ворог", 80, 15)

character1.attack(character2)
