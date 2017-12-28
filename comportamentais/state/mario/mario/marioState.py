from abc import ABC, abstractmethod


class MarioState(ABC):
    """
    Classe abstrata do estados do mario.
    """

    @abstractmethod
    def pega_cogumelo(self):
        """
        Pega o cogumento e faz o mario crescer
        """

        pass

    @abstractmethod
    def pega_flor(self):
        """
        Pega a flor e faz o mário ficar de fogo.
        """

        pass

    @abstractmethod
    def pega_pena(self):
        """
        Pega a pena e faz o mario voar
        """

        pass

    @abstractmethod
    def leva_dano(self):
        """
        Leva dano e morre voltado para o estado inicial.
        """

        pass


class Estado(object):
    """
    Engloba todos os estados em um só
    """

    def __init__(self, estado):
        """
        Importa as classes dos respectivos estados em causar conflitos
        umas com as outras
        """

        if estado == 'MarioPequeno':
            from mario.estados.marioPequeno import MarioPequeno
        elif estado == 'MarioCapa':
            from mario.estados.marioCapa import MarioCapa
        elif estado == 'MarioGrande':
            from mario.estados.marioGrande import MarioGrande
        elif estado == 'MarioFogo':
            from mario.estados.marioFogo import MarioFogo
        else:
            from mario.estados.marioMorto import MarioMorto

        # Eval executa uma código python por um string
        self.__estado = eval(estado)()

    def pega_estado(self):
        """
        Pega o estado e retorna ele.
        """

        return self.__estado
