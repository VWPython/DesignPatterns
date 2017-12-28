from mario.marioState import MarioState, Estado


class MarioPequeno(MarioState):
    """
    Mario no seu estado inicial
    """

    def pega_cogumelo(self):
        print("Mario ficou grande")
        mario = Estado('MarioCapa')
        return mario.pega_estado()

    def pega_flor(self):
        print("Mario ficou grande com poderes de fogo")
        mario = Estado('MarioFogo')
        return mario.pega_estado()

    def pega_pena(self):
        print("Mario ficou grande com capa que voa")
        mario = Estado('MarioCapa')
        return mario.pega_estado()

    def leva_dano(self):
        print("Mario foi morto")
        mario = Estado('MarioMorto')
        return mario.pega_estado()
