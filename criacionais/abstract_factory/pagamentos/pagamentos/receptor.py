from abc import ABC, abstractmethod


class Receptor(ABC):

    @abstractmethod
    def recebe(self):
        pass
