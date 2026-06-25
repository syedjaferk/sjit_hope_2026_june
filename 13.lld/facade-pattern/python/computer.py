class CPU:
    def start(self):
        print("CPU started")


class Memory:
    def load(self):
        print("Memory loaded")


class HardDisk:
    def read(self):
        print("Reading from hard disk")


cpu = CPU()
memory = Memory()
hard_disk = HardDisk()

cpu.start()
memory.load()
hard_disk.read()
