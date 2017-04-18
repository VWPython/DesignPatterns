from carro.fabricas.fiat import Fiat
from carro.fabricas.ford import Ford


def main():

    fabrica = Fiat()
    sedan = fabrica.constroi_carro_sedan()
    popular = fabrica.constroi_carro_popular()
    sedan.mostra_informacao()
    popular.mostra_informacao()

    fabrica = Ford()
    sedan = fabrica.constroi_carro_sedan()
    popular = fabrica.constroi_carro_popular()
    sedan.mostra_informacao()
    popular.mostra_informacao()

if __name__ == "__main__":
    main()
