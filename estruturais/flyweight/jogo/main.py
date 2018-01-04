from jogo import Ponto, FlyweightFactory


def main():
    """
    Compartilhar, de forma eficiente, objetos que são usados em grande
    quantidade.
    """

    factory = FlyweightFactory()

    factory.get_player(factory.sprites['CENARIO_1']).desenha_imagem(Ponto(0, 0))
    factory.get_player(factory.sprites['JOGADOR']).desenha_imagem(Ponto(10, 10))
    factory.get_player(factory.sprites['INIMIGO_1']).desenha_imagem(Ponto(100, 10))
    factory.get_player(factory.sprites['INIMIGO_1']).desenha_imagem(Ponto(120, 10))
    factory.get_player(factory.sprites['INIMIGO_1']).desenha_imagem(Ponto(140, 11))
    factory.get_player(factory.sprites['INIMIGO_2']).desenha_imagem(Ponto(60, 10))
    factory.get_player(factory.sprites['INIMIGO_3']).desenha_imagem(Ponto(50, 10))
    factory.get_player(factory.sprites['CENARIO_2']).desenha_imagem(Ponto(170, 10))


if __name__ == '__main__':
    main()
