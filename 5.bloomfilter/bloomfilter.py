class BloomFilter:
    def __init__(self, size=20):
        self.size = size
        self.bit_array = [0] * size

    def _hash1(self, item):
        return hash(item) % self.size

    def _hash2(self, item):
        return hash("salt1" + item) % self.size

    def _hash3(self, item):
        return hash("salt2" + item) % self.size

    def add(self, item):
        indexes = [
            self._hash1(item),
            self._hash2(item),
            self._hash3(item)
        ]

        for index in indexes:
            self.bit_array[index] = 1

    def contains(self, item):
        indexes = [
            self._hash1(item),
            self._hash2(item),
            self._hash3(item)
        ]

        for index in indexes:
            if self.bit_array[index] == 0:
                return False

        return True

    def display(self):
        print(self.bit_array)


bf = BloomFilter()

bf.add("apple")
bf.add("banana")
bf.add("orange")

print("Bit Array:")
bf.display()

print("\nChecking items:")

items = [
    "apple",
    "banana",
    "mango",
    "grapes"
]

for item in items:
    if bf.contains(item):
        print(f"{item}: Probably Present")
    else:
        print(f"{item}: Definitely Not Present")
