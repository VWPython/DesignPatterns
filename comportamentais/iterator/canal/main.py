from canal.canais import Esporte, Filme


def main():
    """
    Fornecer um modo eficiente para percorrer sequencialmente os
    elementos de uma coleção, sem que a estrutura interna da coleção
    seja exposta.

    Isso pode facilitar a criação de uma lista única independe do tipo
    de lista nativa da liguagem utilizar, por exemplo, List,
    ArrayList, HashMap, ...
    """

    canais_de_esporte = Esporte()
    iterador = canais_de_esporte.criar_iterador()

    print("Canais de esporte:")
    while not iterador.acabou():
        print(iterador.canal_atual())
        iterador.proximo()

    canais_de_filme = Filme()
    iterador = canais_de_filme.criar_iterador()

    print("\nCanais de filme:")
    while not iterador.acabou():
        print(iterador.canal_atual())
        iterador.proximo()


if __name__ == '__main__':
    main()
