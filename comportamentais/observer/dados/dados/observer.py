from abc import ABC, abstractmethod


class Observer(ABC):
    """
    Classe abstrada de criação de observadores para os dados.
    """

    def __init__(self, dados):
        """
        Inicializa os dados observados
        """

        self.dados = dados

    @abstractmethod
    def atualiza(self):
        """
        Atualiza os dados dos objetos observados
        """

        pass
