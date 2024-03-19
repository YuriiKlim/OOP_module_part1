# Завдання 4
# Створіть клас "Комп'ютер", який має зберігати
# інформацію про процесор, ОЗУ та відеокарту. Застосуйте
# інкапсуляцію для захисту цих даних від змін.
class Computer:
    def __init__(self, cpu, ram, gpu):
        self.__cpu = cpu
        self.__ram = ram
        self.__gpu = gpu

    @property
    def cpu(self):
        """Повертає інформацію про процесор."""
        return self.__cpu

    @property
    def ram(self):
        """Повертає інформацію про ОЗУ."""
        return self.__ram

    @property
    def gpu(self):
        """Повертає інформацію про відеокарту."""
        return self.__gpu

    def display_specs(self):
        """Виводить специфікації комп'ютера."""
        print(f"Процесор: {self.cpu}")
        print(f"ОЗУ: {self.ram} GB")
        print(f"Відеокарта: {self.gpu}")

my_computer = Computer("AMD ryzen 5 7500x", 16, "NVIDIA GeForce RTX 4080")
my_computer.display_specs()
