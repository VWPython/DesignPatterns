from mario.estados.marioPequeno import MarioPequeno

class Mario(object):

    def __init__(self):
        self.estado = MarioPequeno()

    def pega_cogumelo(self):
        self.estado = self.estado.pega_cogumelo()

    def pega_flor(self):
        self.estado = self.estado.pega_flor()

    def pega_pena(self):
        self.estado = self.estado.pega_pena()

    def leva_dano(self):
        self.estado = self.estado.leva_dano()
