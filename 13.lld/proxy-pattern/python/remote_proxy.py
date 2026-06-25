from abc import ABC, abstractmethod

class RemoteObject(ABC):
    @abstractmethod
    def perform_action(self):
        pass

class RealRemoteObject(RemoteObject):
    def perform_action(self):
        print("RealRemoteObject performing action")

class RemoteProxy(RemoteObject):
    def __init__(self):
        self._real_object = None

    def perform_action(self):
        if self._real_object is None:
            self._real_object = RealRemoteObject()
        self._real_object.perform_action()

# Client code
proxy = RemoteProxy()
proxy.perform_action()