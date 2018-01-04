from jogo.sprite import Sprite


class FlyweightFactory(object):
    """
    Fabricas de jogadores
    """

    players = []

    sprites = {
        'JOGADOR': 'JOGADOR',
        'INIMIGO_1': 'INIMIGO_1',
        'INIMIGO_2': 'INIMIGO_2',
        'INIMIGO_3': 'INIMIGO_3',
        'CENARIO_1': 'CENARIO_1',
        'CENARIO_2': 'CENARIO_2'
    }

    def __init__(self):
        """
        Insere as sprites de cada player dentro da lista de players
        """

        self.players.append(Sprite("jogador.png"))
        self.players.append(Sprite("inimigo1.png"))
        self.players.append(Sprite("inimigo2.png"))
        self.players.append(Sprite("inimigo3.png"))
        self.players.append(Sprite("cenario1.png"))
        self.players.append(Sprite("cenario2.png"))

    def get_player(self, jogador):
        """
        Pega os players de acordo com a string passada.
        """

        if jogador == 'JOGADOR':
            return self.players[0]
        elif jogador == 'INIMIGO_1':
            return self.players[1]
        elif jogador == 'INIMIGO_2':
            return self.players[2]
        elif jogador == 'INIMIGO_3':
            return self.players[3]
        elif jogador == 'CENARIO_1':
            return self.players[4]
        else:
            return self.players[5]
