from carro.fabricas import Fiat, Volkswagen
from carro import Concessionaria


def main():
    """
    Separar o processo de construção de um objeto de sua representação e
    permitir a sua criação passo-a-passo. Diferentes tipos de objetos podem
    ser criados com implementações distintas de cada passo.
    """

    concessionaria = Concessionaria(Fiat())
    concessionaria.fabrica_carro(
        preco=18000,
        ano_de_fabricacao=2015,
        motor='Total flex 1.4',
        modelo='Uno'
    )
    carro = concessionaria.disponibiliza_carro()
    print("Preço:", carro.preco)
    print("Ano de fabricação:", carro.ano_de_fabricacao)
    print("Motor:", carro.motor)
    print("Modelo:", carro.modelo)
    print("Montadora:", carro.montadora)
    print()

    concessionaria = Concessionaria(Volkswagen())
    concessionaria.fabrica_carro(
        preco=25000,
        ano_de_fabricacao=2017,
        motor='1.0',
        modelo='Celta'
    )
    carro = concessionaria.disponibiliza_carro()
    print("Preço:", carro.preco)
    print("Ano de fabricação:", carro.ano_de_fabricacao)
    print("Motor:", carro.motor)
    print("Modelo:", carro.modelo)
    print("Montadora:", carro.montadora)


if __name__ == '__main__':
    main()
