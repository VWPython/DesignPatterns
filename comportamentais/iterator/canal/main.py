from canal.canais import Esporte, Filme


def main():
    """
    Função principal
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
