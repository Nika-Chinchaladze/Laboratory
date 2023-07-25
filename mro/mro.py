class Animal:
    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.legs = 4

    def walking(self):
        return "Animal can walk..."

    def running(self):
        return "Animal can run..."


class Dog(Animal):
    def __init__(self, color, name):
        super().__init__(color, name)

    def walking(self):
        return "Dog can walk..."


class Cat(Animal):
    def __init__(self, color, name):
        super().__init__(color, name)

    def walking(self):
        return "Cat can walk..."


class Nadira(Cat, Dog):
    def __init__(self, color, name):
        super().__init__(color, name)


my_obj = Nadira(color="black", name="nadira")
print(my_obj.walking())
print(my_obj.running())
print(Nadira.__mro__)
