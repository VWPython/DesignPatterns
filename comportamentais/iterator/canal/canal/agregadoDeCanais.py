from abc import ABC, abstractmethod


class AgregadoDeCanais(ABC):
    """
    Define a interface das coleções de canais que podem ter seus elementos
    percorridos através de um Iterador.
    """

    @abstractmethod
    def criar_iterador(self):
        """
        Cria o iterador de canais
        """

        pass
