from carro.concessionaria import Concessionaria
from carro.fabricas.fiat import Fiat
from carro.fabricas.volkswagen import Volkswagen

def main():
    concessionaria = Concessionaria(Fiat())
    concessionaria.fabrica_carro()
    carro = concessionaria.disponibiliza_carro()
    print("Preço:", carro.preco)
    print("Motor:", carro.motor)
    print("Ano de fabricação:", carro.ano_de_fabricacao)
    print("Modelo:", carro.modelo)
    print("Montadora:", carro.montadora)
    print()

    concessionaria = Concessionaria(Volkswagen())
    concessionaria.fabrica_carro()
    carro = concessionaria.disponibiliza_carro()
    print("Preço:", carro.preco)
    print("Motor:", carro.motor)
    print("Ano de fabricação:", carro.ano_de_fabricacao)
    print("Modelo:", carro.modelo)
    print("Montadora:", carro.montadora)

if __name__ == '__main__':
    main()
