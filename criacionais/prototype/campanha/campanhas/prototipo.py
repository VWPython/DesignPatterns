from abc import ABC, abstractmethod


class Prototipo(ABC):

    @abstractmethod
    def clone(self):
        pass
