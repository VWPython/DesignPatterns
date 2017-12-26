from mario.marioState import MarioState


class MarioMorto(MarioState):

    def __init__(self):
        print("Mario voltou a ser pequeno")

    def pega_cogumelo(self):
        return MarioGrande()

    def pega_flor(self):
        return MarioFogo()

    def pega_pena(self):
        return MarioCapa()

    def leva_dano(self):
        return MarioMorto()
