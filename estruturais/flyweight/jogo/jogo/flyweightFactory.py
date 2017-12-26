from jogo.sprite import Sprite

class FlyweightFactory(object):
    flyweights = []
    sprites = {
        'JOGADOR':'JOGADOR',
        'INIMIGO_1':'INIMIGO_1',
        'INIMIGO_2':'INIMIGO_2',
        'INIMIGO_3':'INIMIGO_3',
        'CENARIO_1':'CENARIO_1',
        'CENARIO_2':'CENARIO_2'
    }

    def __init__(self):
        self.flyweights.append(Sprite("jogador.png"))
        self.flyweights.append(Sprite("inimigo1.png"))
        self.flyweights.append(Sprite("inimigo2.png"))
        self.flyweights.append(Sprite("inimigo3.png"))
        self.flyweights.append(Sprite("cenario1.png"))
        self.flyweights.append(Sprite("cenario2.png"))

    def get_flyweight(self, jogador):
        if jogador == 'JOGADOR':
            return self.flyweights[0]
        elif jogador == 'INIMIGO_1':
            return self.flyweights[1]
        elif jogador == 'INIMIGO_2':
            return self.flyweights[2]
        elif jogador == 'INIMIGO_3':
            return self.flyweights[3]
        elif jogador == 'CENARIO_1':
            return self.flyweights[4]
        else:
            return self.flyweights[5]
