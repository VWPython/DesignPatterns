from abc import ABC, abstractmethod


class FabricaDeComunicadores(ABC):

    @abstractmethod
    def cria_emissor(self):
        pass

    @abstractmethod
    def cria_receptor(self):
        pass
