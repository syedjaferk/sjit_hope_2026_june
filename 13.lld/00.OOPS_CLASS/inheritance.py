class Animal:
    def __init__(self, name="") -> None:
        self.name = name

    def eat(self):
        print("Animal Eating")

    def sleep(self):
        print("sleeping")

    def print_name(self):
        print(self.name)


class Dog(Animal):
    def eat(self):
        print("Eating Chicken Biryani")
        # super().eat()


class GermanShepard(Dog):
    def __init__(self, name="") -> None:
        super(Dog, self).__init__(name)

    def eat(self):
        super(Dog, self).eat()


d = GermanShepard(name="")
d.eat()
d.print_name()
# d.sleep()
