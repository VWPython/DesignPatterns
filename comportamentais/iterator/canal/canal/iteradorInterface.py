from abc import ABC, abstractmethod


class IteradorInterface(ABC):
    """
    Define a interface dos canais que encapsulam toda a complexidade
    para percorrer os elementos do Agregador de canais.
    """

    @abstractmethod
    def primeiro(self):
        """
        Primeiro elemento do iterador
        """

        pass

    @abstractmethod
    def proximo(self):
        """
        Próximo elemento do iterador
        """

        pass

    @abstractmethod
    def acabou(self):
        """
        Iterador chegou no seu último elemento
        """

        pass

    @abstractmethod
    def canal_atual(self):
        """
        Pega o item atual do iterador.
        """

        pass
