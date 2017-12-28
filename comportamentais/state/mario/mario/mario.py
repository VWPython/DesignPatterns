from mario.marioState import Estado
from mario.estados.marioPequeno import MarioPequeno


class Mario(object):
    """
    Classe responsavel por criar os estados do Mario.
    """

    def __init__(self):
        """
        Faz o mario começar pequeno.
        """

        self.estado = MarioPequeno()

    def pega_cogumelo(self):
        """
        Pega o cogumento e faz o mario crescer
        """

        self.estado = self.estado.pega_cogumelo()

    def pega_flor(self):
        """
        Pega a flor e faz o mário ficar de fogo.
        """

        self.estado = self.estado.pega_flor()

    def pega_pena(self):
        """
        Pega a pena e faz o mario voar
        """

        self.estado = self.estado.pega_pena()

    def leva_dano(self):
        """
        Leva dano e morre voltado para o estado inicial.
        """

        self.estado = self.estado.leva_dano()
