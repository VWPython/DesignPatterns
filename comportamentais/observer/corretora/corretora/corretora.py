from abc import ABC, abstractmethod


class Observador(ABC):
    """
    Classe abstrata responsavel pela criação de observadores das ações
    bolsa de valores.
    """

    @abstractmethod
    def notifica_alteracao(self, acao):
        """
        Notifica alterações na ação da bolsa de valores.
        """

        pass
