from mario.marioState import MarioState, Estado


class MarioFogo(MarioState):
    """
    Pega a flor e faz o mário ficar de fogo.
    """

    def pega_cogumelo(self):
        print("Mario ganhou 1000 pontos")
        mario = Estado('MarioGrande')
        return mario.pega_estado()

    def pega_flor(self):
        print("Mario ganhou 1000 pontos")
        mario = Estado('MarioFogo')
        return mario.pega_estado()

    def pega_pena(self):
        print("Mario ganhou pena e pode voar")
        mario = Estado('MarioCapa')
        return mario.pega_estado()

    def leva_dano(self):
        print("Mario foi morto")
        mario = Estado('MarioMorto')
        return mario.pega_estado()
