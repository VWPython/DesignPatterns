from mario.marioState import MarioState
from mario.estados.marioCapa import MarioCapa

class MarioGrande(MarioState):

    def pega_cogumelo(self):
        print("Mario ganhou 1000 pontos")
        return MarioGrande()

    def pega_flor(self):
        print("Mario ficou com poderes de fogo")
        return MarioFogo()

    def pega_pena(self):
        print("Mario ficou com capa que voa")
        return MarioCapa()

    def leva_dano(self):
        print("Mario foi morto")
        return MarioMorto()
