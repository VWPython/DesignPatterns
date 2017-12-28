from mario.marioState import MarioState, Estado


class MarioCapa(MarioState):
    """
    Pega a pena e faz o mario voar
    """

    def pega_cogumelo(self):
        print("Mario ganhou 1000 pontos")
        mario = Estado('MarioGrande')
        return mario.pega_estado()

    def pega_flor(self):
        print("Mario com poderes de fogo")
        mario = Estado('MarioFogo')
        return mario.pega_estado()

    def pega_pena(self):
        print("Mario ganhou 1000 pontos")
        mario = Estado('MarioCapa')
        return mario.pega_estado()

    def leva_dano(self):
        print("Mario foi morto")
        mario = Estado('MarioMorto')
        return mario.pega_estado()
