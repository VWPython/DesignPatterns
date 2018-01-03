from carro.fabricas import Fiat, Ford


def main():
    """
    Função principal
    """

    fabrica = Fiat()
    sedan = fabrica.constroi_carro_sedan(Fiat.WEEKEND)
    sedan.mostra_informacao()
    sedan = fabrica.constroi_carro_sedan(Fiat.SIENA)
    sedan.mostra_informacao()
    popular = fabrica.constroi_carro_popular(Fiat.PALIO)
    popular.mostra_informacao()
    popular = fabrica.constroi_carro_popular(Fiat.UNO)
    popular.mostra_informacao()

    fabrica = Ford()
    sedan = fabrica.constroi_carro_sedan(Ford.FIESTA_SEDAN)
    sedan.mostra_informacao()
    sedan = fabrica.constroi_carro_sedan(Ford.KA_SEDAN)
    sedan.mostra_informacao()
    popular = fabrica.constroi_carro_popular(Ford.FIESTA)
    popular.mostra_informacao()
    popular = fabrica.constroi_carro_popular(Ford.KA)
    popular.mostra_informacao()


if __name__ == "__main__":
    main()
