from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def add(self, component):
        pass

    @abstractmethod
    def remove(self, component):
        pass

    @abstractmethod
    def get_price(self):
        pass
