
# Багаторівневе успадкування
class GrandParent:
    def go(self):
        print('I go')

    def method(self):
        print('GrandParent method')


class Parent(GrandParent):
    def walk(self):
        print('I walk')

    def go(self):
        print('Parent go')

    def method(self):
        print('Parent method')


class Child(Parent):
    def method(self):
        print('Child method')


# child = Child()
# child.go()
# child.walk()
# child.method()


# Множинне успадкування
class ClassA:
    def methodA(self):
        print('hello from A')

    def method(self):
        print('method from A')


class ClassB:
    def methodB(self):
        print('hello from B')

    def method(self):
        print('method from B')


class ClassC(ClassA, ClassB):
    def methodA(self):
        print('modified methodA')

    def get_super(self):
        print(super().methodA())


obj = ClassC()
# obj.methodA()
# obj.methodB()
# obj.method()

# print(Child.__mro__)
#
# print(Child.mro())
# child = Child()
# child.method()

# import time
# print(type(time).__mro__)
#
#
# def func():
#     return 1
#
# print(type(func))
#
# func.attr = 3
# print(func.attr)

#print(ClassC.mro())
print(obj.get_super())



class GrandParent:
    def __init__(self, history):
        self.history = history


class Parent(GrandParent):
    def __init__(self, history, family_info):
        super().__init__(history)
        self.family_info = family_info


class Child(Parent):
    def __init__(self, history, family_info, dreams):
        super().__init__(history, family_info)
        self.dreams = dreams

    def get_info(self):
        print(self.history)
        print(self.family_info)
        print(self.dreams)


# child = Child('history', 'family', 'dreams')
# child.get_info()

# Множинне успадкування
class ClassA:
    def __init__(self, a):
        self.a = a


class ClassB:
    def __init__(self, b):
        self.b = b


class ClassC(ClassA, ClassB):
    def __init__(self, a, b, c):
        super().__init__(a)
        ClassB.__init__(self, b)
        self.c = c

    def get_info(self):
        print(self.a)
        print(self.b)
        print(self.c)


obj = ClassC(1, 2, 3)
obj.get_info()



class UIElement:
    def __init__(self, functionality):
        self.functionality = functionality

    def display(self):
        print('display UIElement')


class InteractiveElement:
    def __init__(self, a, b):
        pass

    def click(self):
        print('click, click')


class Button(UIElement, InteractiveElement):
    def __init__(self, functionality, label):
        super().__init__(functionality)
        self.label = label

    def display(self):
        print('display button')


class Menu(UIElement, InteractiveElement):
    def __init__(self, functionality, info):
        super().__init__(functionality)
        self.info = info

    def display(self):
        print('display Menu')


class FieldInput(UIElement, InteractiveElement):
    def __init__(self, functionality, text):
        super().__init__(functionality)
        self.text = text

    def display(self):
        print('display Field')


button = Button('', 'Open')
menu = Menu('', 'very useful program')
field = FieldInput('', 'Your login')

button.display()
menu.display()
field.display()

button.click()
menu.click()
field.click()



class CPU:
    def __init__(self, num_kernel):
        print('init from CPU')
        self.num_kernel = num_kernel


class GPU:
    def __init__(self, memmory):
        print('init from GPU')
        self.memmory = memmory


class RAM:
    def __init__(self, capacity):
        print('init from RAM')
        self.capacity = capacity


class Motherboard:
    def __init__(self, type_socket):
        print('init from Motherboard')
        self.type_socket = type_socket


class Computer(CPU, GPU, RAM, Motherboard):
    def __init__(self, num_kernel, memmory, capacity, type_socket):
        print(f'init from {type(self).__name__}')
        super().__init__(num_kernel)
        GPU.__init__(self, memmory)
        RAM.__init__(self, capacity)
        Motherboard.__init__(self, type_socket)


obj = Computer(1, 200, 30, 'type')
