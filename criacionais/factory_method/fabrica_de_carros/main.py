from carro.fabricas import Fiat, Volkswagen, Ford, Chevrolet


def main():
    """
    Encapsula a escolha da classe concreta a ser utilizada na criação de
    objetos de um determinado tipo

    A fábrica (interface) cria objetos que só serão definidos em tempo de
    execução pela suas subclasses
    """

    fabrica = Fiat()
    carro = fabrica.constroi_carro(Fiat.UNO)
    carro.mostra_informacao()
    carro = fabrica.constroi_carro(Fiat.PALIO)
    carro.mostra_informacao()

    fabrica = Volkswagen()
    carro = fabrica.constroi_carro(Volkswagen.GOL)
    carro.mostra_informacao()
    carro = fabrica.constroi_carro(Volkswagen.CROSSFOX)
    carro.mostra_informacao()

    fabrica = Ford()
    carro = fabrica.constroi_carro(Ford.KA)
    carro.mostra_informacao()
    carro = fabrica.constroi_carro(Ford.FIESTA)
    carro.mostra_informacao()

    fabrica = Chevrolet()
    carro = fabrica.constroi_carro(Chevrolet.PRISMA)
    carro.mostra_informacao()
    carro = fabrica.constroi_carro(Chevrolet.CELTA)
    carro.mostra_informacao()


if __name__ == "__main__":
    main()
