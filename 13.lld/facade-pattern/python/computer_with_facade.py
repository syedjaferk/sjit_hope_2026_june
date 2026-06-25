class CPU:
    def start(self):
        print("CPU started")


class Memory:
    def load(self):
        print("Memory loaded")


class HardDisk:
    def read(self):
        print("Reading from hard disk")


class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_disk = HardDisk()

    def start(self):
        self.cpu.start()
        self.memory.load()
        self.hard_disk.read()

        print("Computer started")


computer = ComputerFacade()
computer.start()
