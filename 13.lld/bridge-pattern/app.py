from abc import ABC, abstractmethod


# Abstraction
class Animals(ABC):
    def __init__(self, move_logic):
        self.move_logic = move_logic

    @abstractmethod
    def move(self):
        pass


# Implementation - Move
class Move(ABC):
    @abstractmethod
    def move(self):
        pass


# Concrete Implementation
class Walk(Move):
    def move(self):
        print("Movement is walking")


# Concrete Implementation
class Fly(Move):
    def move(self):
        print("Movement is flying")


# Concrete Implementation
class Swim(Move):
    def move(self):
        print("Movement is Swiming")


# Concrete Abstraction
class Person(Animals):
    def __init__(self, move_logic: Move):
        self.move_logic = move_logic

    def move(self):
        self.move_logic.move()


# Concrete Abstraction
class Bird(Animals):
    def __init__(self, move_logic: Move):
        self.move_logic = move_logic

    def move(self):
        self.move_logic.move()


# Concrete Abstraction
class Fish(Animals):
    def __init__(self, move_logic: Move):
        self.move_logic = move_logic

    def move(self):
        self.move_logic.move()


def client_code():
    gold_fish = Fish(move_logic=Swim())
    gold_fish.move()


client_code()
