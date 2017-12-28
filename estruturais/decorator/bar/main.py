from bar.bebidas.cachaca import Cachaca
from bar.adicionais.acuca import Acuca
from bar.adicionais.suco import Suco


def main():
    coquetel = Cachaca()
    print(coquetel.get_nome() + " = R$ " + str(coquetel.get_preco()))

    coquetel = Suco(coquetel)
    print(coquetel.get_nome() + " = R$ " + str(coquetel.get_preco()))

    coquetel = Acuca(coquetel)
    print(coquetel.get_nome() + " = R$ " + str(coquetel.get_preco()))


if __name__ == '__main__':
    main()
