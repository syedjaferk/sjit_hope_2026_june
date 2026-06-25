import os
import random
import time

import psutil

# ----------------------------
# Flyweight
# ----------------------------


class TreeType:
    def __init__(self, name):
        self.name = name

        print(f"Loading assets for {name}...")

        # Simulate heavy assets

        self.texture = bytearray(2 * 1024 * 1024)  # 2 MB
        self.mesh = bytearray(1 * 1024 * 1024)  # 1 MB
        self.sound = bytearray(1 * 1024 * 1024)  # 1 MB

    def render(self, x, y):
        pass


# ----------------------------
# Flyweight Factory
# ----------------------------


# Singleton Design Pattern
class TreeFactory:
    _tree_types = {}

    @classmethod
    def get_tree_type(cls, name):
        if name not in cls._tree_types:
            cls._tree_types[name] = TreeType(name)

        return cls._tree_types[name]


# ----------------------------
# Context Object
# ----------------------------


class Tree:
    def __init__(self, x, y, tree_type):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def draw(self):
        self.tree_type.render(self.x, self.y)


# ----------------------------
# Forest
# ----------------------------


class Forest:
    def __init__(self):
        self.trees = []

    def plant_tree(self, tree_type_name, x, y):
        tree_type = TreeFactory.get_tree_type(tree_type_name)

        self.trees.append(Tree(x, y, tree_type))


# ----------------------------
# Game Loop
# ----------------------------

forest = Forest()

process = psutil.Process(os.getpid())

counter = 0

while True:
    forest.plant_tree(
        "Oak",
        random.randint(0, 1000),
        random.randint(0, 1000),
    )

    counter += 1

    if counter % 1000 == 0:
        mem = process.memory_info().rss / 1024 / 1024

        print(f"Trees={counter} Memory={mem:.2f} MB")

    time.sleep(0.001)
