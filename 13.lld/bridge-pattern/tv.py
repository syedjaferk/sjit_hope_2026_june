from abc import ABC, abstractmethod

# Implementation


class TV(ABC):
    @abstractmethod
    def turn_on(self):
        pass


class SonyTV(TV):
    def turn_on(self):
        print("Turned On SONY TV")


class SamsungTV(TV):
    def turn_on(self):
        print("Turned On Samsung TV")


# Abstraction - High Level Control
class Remote:
    def __init__(self, tv) -> None:
        self.tv = tv

    def power(self):
        self.tv.turn_on()


class SmartRemote(Remote):
    def voice_control(self):
        print("Voice Control Activated")


sony = SonyTV()
remote = SmartRemote(sony)

remote.power()
remote.voice_control()
