from abc import ABC, abstractmethod


# Component (Leaf)
class Component(ABC):
    @abstractmethod
    def get_price(self):
        pass


# Leaf
class Transistor(Component):
    def get_price(self):
        return 10  # Just an arbitrary value for demonstration


# Leaf
class Chip(Component):
    def get_price(self):
        return 20  # Just an arbitrary value for demonstration


# Leaf
class Valve(Component):
    def get_price(self):
        return 15  # Just an arbitrary value for demonstration


# Leaf
class Tire(Component):
    def get_price(self):
        return 50  # Just an arbitrary value for demonstration


# Composite
class Composite(Component):
    def __init__(self, name):
        self.name = name
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def get_price(self):
        total_price = sum(component.get_price() for component in self.components)
        return total_price


# Client code
if __name__ == "__main__":
    # Creating leaf objects
    transistor = Transistor()
    chip = Chip()
    valve = Valve()
    tire = Tire()

    # Creating composite objects
    electrical_components = Composite("Electrical Components")
    electrical_components.add_component(transistor)
    electrical_components.add_component(chip)
    electrical_components.add_component(valve)

    engine = Composite("Engine")
    engine.add_component(electrical_components)

    car = Composite("Car")
    car.add_component(engine)
    car.add_component(tire)

    # Applying operation on leaf objects
    print(f"Transistor Price: {transistor.get_price()}")
    print(f"Chip Price: {chip.get_price()}")
    print(f"Valve Price: {valve.get_price()}")
    print(f"Tire Price: {tire.get_price()}")

    # Applying operation on composite objects
    print(f"Engine Price: {engine.get_price()}")
    print(f"Car Price: {car.get_price()}")
