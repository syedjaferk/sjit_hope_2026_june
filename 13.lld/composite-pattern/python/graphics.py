 from abc import ABC, abstractmethod

 # Component
 class Graphic(ABC):
     @abstractmethod
     def draw(self):
         pass

 # Leaf
 class Circle(Graphic):
     def draw(self):
         print("Drawing Circle")

 # Leaf
 class Square(Graphic):
     def draw(self):
         print("Drawing Square")

 # Composite
 class CompositeGraphic(Graphic):
     def __init__(self):
         self.graphics = []

     def add(self, graphic):
         self.graphics.append(graphic)

     def draw(self):
         print("Drawing Composite:")
         for graphic in self.graphics:
             graphic.draw()

 # Usage
 circle = Circle()
 square = Square()
 composite = CompositeGraphic()
 composite.add(circle)
 composite.add(square)

 composite.draw()
