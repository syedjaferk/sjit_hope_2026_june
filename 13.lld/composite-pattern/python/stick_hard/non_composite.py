class Circle:
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        print(f"Drawing Circle with radius {self.radius}")


class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def draw(self):
        print(f"Drawing Square with side length {self.side_length}")


# Usage
circles = [Circle(5) for _ in range(500000)]
squares = [Square(4) for _ in range(500000)]

for circle in circles:
    circle.draw()

for square in squares:
    square.draw()
