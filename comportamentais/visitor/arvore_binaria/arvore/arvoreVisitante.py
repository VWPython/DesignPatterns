from abc import ABC, abstractmethod


class ArvoreVisitante(ABC):
    """
    Classe abstrata para criar visitantes na arvore de busca.
    """

    @abstractmethod
    def visitar(self, no):
        """
        Visita a arvore de busca.
        """

        pass
