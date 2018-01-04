from trecho import Caminho
from trecho.trechos import Andando, Carro


def main():
    """
    Agrupa objetos que fazem parte de uma relação parte-todo de forma a
    tratá-los sem distinção
    """

    trecho1 = Andando(
        "Vá até o cruzamento da Av. Rebouças com a Av. Brigadeiro Faria",
        500
    )

    trecho2 = Carro(
        "Vá até o cruzamento da Av. Brigadeiro com a Av. Cidade Jardim",
        1500
    )

    trecho3 = Carro(
        "Vire a direita na Marginal Pinheiros",
        500
    )

    caminho1 = Caminho()
    caminho1.adiciona(trecho1)
    caminho1.adiciona(trecho2)

    print("**** Caminho 01 ****")
    caminho1.imprime()

    caminho2 = Caminho()
    caminho2.adiciona(caminho1)
    caminho2.adiciona(trecho3)

    print("\n**** Caminho 02 ****")
    caminho1.imprime()


if __name__ == '__main__':
    main()
