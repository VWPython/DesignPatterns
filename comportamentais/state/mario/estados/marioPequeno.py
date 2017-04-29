from mario.marioState import MarioState
from mario.estados.marioGrande import MarioGrande

class MarioPequeno(MarioState):

    def pega_cogumelo(self):
        print("Mario ficou grande")
        return MarioGrande()

    def pega_flor(self):
        print("Mario ficou grande com poderes de fogo")
        return MarioFogo()

    def pega_pena(self):
        print("Mario ficou grande com capa que voa")
        return MarioCapa()

    def leva_dano(self):
        print("Mario foi morto")
        return MarioMorto()
