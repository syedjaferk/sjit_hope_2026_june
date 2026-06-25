class Graphic:
    def draw(self):
        pass

class Circle(Graphic):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        print(f"Drawing Circle with radius {self.radius}")

class Square(Graphic):
    def __init__(self, side_length):
        self.side_length = side_length

    def draw(self):
        print(f"Drawing Square with side length {self.side_length}")

class CompositeGraphic(Graphic):
    def __init__(self):
        self.graphics = []

    def add(self, graphic):
        self.graphics.append(graphic)

    def draw(self):
        for graphic in self.graphics:
            graphic.draw()

# Usage
composite = CompositeGraphic()
for _ in range(500000):
    composite.add(Circle(5))

for _ in range(500000):
    composite.add(Square(4))

composite.draw()
