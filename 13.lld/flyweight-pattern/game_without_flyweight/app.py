import random
import time


class Tree:
    def __init__(self, tree_type, x, y):
        self.tree_type = tree_type
        self.x = x
        self.y = y

        # Simulate expensive assets

        self.texture = bytearray(2 * 1024 * 1024)  # 2 MB
        self.mesh = bytearray(1 * 1024 * 1024)  # 1 MB
        self.sound = bytearray(1 * 1024 * 1024)  # 1 MB

    def draw(self):
        pass


class Forest:
    def __init__(self):
        self.trees = []

    def plant_tree(self, tree_type, x, y):
        self.trees.append(Tree(tree_type, x, y))


forest = Forest()

counter = 0

while True:
    forest.plant_tree(
        "Oak",
        random.randint(0, 1000),
        random.randint(0, 1000),
    )

    counter += 1

    if counter % 50 == 0:
        print(f"Trees: {counter}")

    # time.sleep(0.1)
