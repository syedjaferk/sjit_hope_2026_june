from abc import ABC, abstractmethod


# Interface -> Structure.
class RealObjectService:
    @abstractmethod
    def perform_action(self):  # Blueprint or Enforcement
        pass


class RealObject(RealObjectService):
    def perform_action(self):  # Implementation
        print("RealObject performing action")


class Proxy(RealObjectService):
    def __init__(self):
        self._real_object = None

    def perform_action(self):
        print("from proxy")
        if self._real_object is None:
            self._real_object = RealObject()
        self._real_object.perform_action()


# Client code
proxy = Proxy()
proxy.perform_action()
