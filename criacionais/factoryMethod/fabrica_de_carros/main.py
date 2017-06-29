from carro.fabricas.fiat import Fiat
from carro.fabricas.volkswagen import Volkswagen
from carro.fabricas.ford import Ford
from carro.fabricas.chevrolet import Chevrolet


def main():

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
