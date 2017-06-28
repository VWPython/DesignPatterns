from carro.fabricas.fiat import Fiat
from carro.fabricas.volkswagen import Volkswagen
from carro.fabricas.ford import Ford
from carro.fabricas.chevrolet import Chevrolet

def main():

    fabrica = Fiat()
    carro = fabrica.constroi_carro()
    carro.mostra_informacao();

    fabrica = Volkswagen()
    carro = fabrica.constroi_carro()
    carro.mostra_informacao();

    fabrica = Ford()
    carro = fabrica.constroi_carro()
    carro.mostra_informacao();

    fabrica = Chevrolet()
    carro = fabrica.constroi_carro()
    carro.mostra_informacao();

if __name__ == "__main__":
    main()
