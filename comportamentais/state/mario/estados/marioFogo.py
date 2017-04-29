from mario.marioState import MarioState

class MarioFogo(MarioState):

    def pega_cogumelo(self):
        print("Mario ganhou 1000 pontos")
        return MarioGrande()

    def pega_flor(self):
        print("Mario ganhou 1000 pontos")
        return MarioFogo()

    def pega_pena(self):
        print("Mario ganhou pena e pode voar")
        return MarioCapa()

    def leva_dano(self):
        print("Mario foi morto")
        return MarioMorto()
